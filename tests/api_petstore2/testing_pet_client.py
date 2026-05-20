from pet_client import PetClient;
import pytest;
import json;
# before each test, we need to create a new instance of the PetClient class 
@pytest.fixture
def pet_client_fixture():
    return PetClient()

@pytest.fixture
def get_pet_id_fixture(pet_client_fixture):
    create_pet = pet_client_fixture.add_new_pet("Fluffy", "Pytest")
    newpet_id = create_pet.json()['id']
    return newpet_id

@pytest.mark.skip(reason="This test is currently skipped because it is not implemented yet.")
def test_get_new_pet(pet_client_fixture, get_pet_id_fixture):
    newpet = pet_client_fixture.get_pet(get_pet_id_fixture)
    assert newpet.status_code == 200

# negative get pet test 
#@pytest.mark.xfail(reason="This test is expected to fail because it is testing the negative scenario of getting a pet with an invalid ID.")
def test_get_new_pet_negative(pet_client_fixture):
    with pytest.raises(ValueError):
        pet_client_fixture.get_pet(123456789) 

def test_addPet2(pet_client_fixture):
    newpet = pet_client_fixture.add_new_pet("Spot", "Pytest")
    assert newpet.status_code == 200
    body = newpet.json();
    assert body['name'] == "Spot"
    assert body['category']['name'] == "Pytest"

def test_addPet3(pet_client_fixture):
    newpet = pet_client_fixture.add_new_pet(12, "Pytest")
    assert newpet.status_code == 200

# same test but with parameterization ( test.each and DataProvider in Java )
@pytest.mark.parametrize("name, category_name", [
    ("Fluffy", "Pytest"),
    ("Spot", "Pytest"),
    ("Buddy", "Pytest"),
    ("Gold", "Pytest")
])
def test_addPet_parametrized(pet_client_fixture, name, category_name):
    newpet = pet_client_fixture.add_new_pet(name, category_name)
    assert newpet.status_code == 200
    body = newpet.json();
    assert body['name'] == name


# validate fields in the response body
#sample : 
# {'id': 12345, 
# 'category': {'id': 1, 'name': 'Pytest'}, 
# 'name': '12', 
# 'photoUrls': ['http://example.com/photo1.jpg'], 
# 'tags': [{'id': 1, 'name': 'tag1'}], 
# 'status': 'available'}

def test_validate_response_fields(pet_client_fixture):
    fields = ["id", "category", "name", "photoUrls", "tags", "status"]
    add_pet_response = pet_client_fixture.add_new_pet("Bobby", "NewCat")
    for field in fields: 
        assert add_pet_response.json()[field] is not None, f"Field '{field}' is missing in the response body"


# parse JSON response and validate specific fields
def test_validate_response_fields_values(pet_client_fixture):
    add_pet_response = pet_client_fixture.add_new_pet("Charlie", "NewDog")
    response_json = add_pet_response.json()
    assert response_json['name'] == "Charlie", "Pet name does not match"
    assert response_json['category']['name'] == "NewDog", "Category name does not match"
    for url in response_json['photoUrls']:
        assert url.startswith("http://"), f"Photo URL '{url}' does not start with 'http://'"
    assert response_json['status'] in ["available", "pending", "sold"], "Status value is not valid"
    all_tags = response_json['tags']
    assert isinstance(all_tags, list), "Tags should be a list"
    assert len(all_tags) > 0, "Tags list should not be empty"
    for tag in all_tags:
        assert 'id' in tag and 'name' in tag, "Each tag should have 'id' and 'name'"
        assert isinstance(tag['id'], int), "Tag 'id' should be an integer"
        assert isinstance(tag['name'], str), "Tag 'name' should be a string"
        assert tag['name'] != "", "Tag 'name' should not be empty"
    assert response_json['tags'][0]['name'] == "tag1", "Tag name does not match"
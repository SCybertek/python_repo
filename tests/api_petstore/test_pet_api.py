def test_create_fetch_update_and_delete_pet(api_client, pet_payload):
    create_response = api_client.request("POST", "/pet", json_body=pet_payload)
    assert create_response.status_code == 200
    assert create_response.body["id"] == pet_payload["id"]

    get_response = api_client.request("GET", f"/pet/{pet_payload['id']}")
    assert get_response.status_code == 200
    assert get_response.body["name"] == pet_payload["name"]

    updated_pet = {
        **pet_payload,
        "name": f"{pet_payload['name']}-updated",
        "status": "sold",
    }
    update_response = api_client.request("PUT", "/pet", json_body=updated_pet)
    assert update_response.status_code == 200
    assert update_response.body["status"] == "sold"

    updated_get_response = api_client.request("GET", f"/pet/{pet_payload['id']}")
    assert updated_get_response.status_code == 200
    assert updated_get_response.body["name"] == updated_pet["name"]

    delete_response = api_client.request(
        "DELETE",
        f"/pet/{pet_payload['id']}",
        headers={"api_key": "special-key"},
    )
    assert delete_response.status_code == 200


def test_find_pets_by_status(api_client):
    response = api_client.request("GET", "/pet/findByStatus", params={"status": "available"})
    assert response.status_code == 200
    assert isinstance(response.body, list)


def test_missing_pet_returns_not_found(api_client):
    response = api_client.request("GET", "/pet/999999999999999")
    assert response.status_code == 404

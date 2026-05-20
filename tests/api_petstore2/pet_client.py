import requests;
import random;

class PetClient:

    # constructor to initialize the base URL for the API
    def __init__(self, base_url = "https://petstore.swagger.io/v2"):
        self.base_url = base_url

    # method for Pet
    def add_new_pet(self, name, category_name):
        # code to add a new pet to the store using the API
        json_body = {
            "id": random.randint(10000, 99999),
            "name": name,
            "category": {"id": 1, "name": category_name},
            "photoUrls": ["http://example.com/photo1.jpg"],
            "tags": [{"id": 1, "name": "tag1"}],
            "status": "available"
        }
        # sending response to URL
        response = requests.post(f"{self.base_url}/pet", json=json_body)
        print("Response body:", response.json())
        return response
    
# note :   At that point, you are calling the method while Python is still defining the class.
# But add_new_pet is an instance method, so it expects self as its first argument:

#print(newpet.json())


    def get_pet(self, id):
        response = requests.get(f"{self.base_url}/pet/{id}")
        if response.status_code == 200:
            return response
        else:
            raise ValueError(f"Pet with id {id} not found. Status code: {response.status_code}")


# pet_client = PetClient() # initialize the PetClient with the base URL
# newpet = pet_client.add_new_pet("Fluffy", "Pytest");
# myId = newpet.json()['id']
# print("my new pet id", myId)
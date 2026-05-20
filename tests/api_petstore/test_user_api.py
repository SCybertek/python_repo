def test_create_fetch_update_login_logout_and_delete_user(api_client, user_payload):
    create_response = api_client.request("POST", "/user", json_body=user_payload)
    assert create_response.status_code == 200

    get_response = api_client.request("GET", f"/user/{user_payload['username']}")
    assert get_response.status_code == 200
    assert get_response.body["email"] == user_payload["email"]

    updated_user = {
        **user_payload,
        "firstName": "Updated",
        "phone": "555-0199",
    }
    update_response = api_client.request(
        "PUT",
        f"/user/{user_payload['username']}",
        json_body=updated_user,
    )
    assert update_response.status_code == 200

    updated_get_response = api_client.request("GET", f"/user/{user_payload['username']}")
    assert updated_get_response.status_code == 200
    assert updated_get_response.body["firstName"] == "Updated"

    login_response = api_client.request(
        "GET",
        "/user/login",
        params={
            "username": user_payload["username"],
            "password": user_payload["password"],
        },
    )
    assert login_response.status_code == 200
    assert login_response.body["code"] == 200
    assert "logged in user session" in login_response.body["message"]

    logout_response = api_client.request("GET", "/user/logout")
    assert logout_response.status_code == 200

    delete_response = api_client.request("DELETE", f"/user/{user_payload['username']}")
    assert delete_response.status_code == 200

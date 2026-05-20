def test_inventory_returns_status_counts(api_client):
    response = api_client.request("GET", "/store/inventory", headers={"api_key": "special-key"})
    assert response.status_code == 200
    assert isinstance(response.body, dict)


def test_create_fetch_and_delete_order(api_client, order_payload):
    create_response = api_client.request("POST", "/store/order", json_body=order_payload)
    assert create_response.status_code == 200
    assert create_response.body["id"] == order_payload["id"]

    get_response = api_client.request("GET", f"/store/order/{order_payload['id']}")
    assert get_response.status_code == 200
    assert get_response.body["petId"] == order_payload["petId"]

    delete_response = api_client.request("DELETE", f"/store/order/{order_payload['id']}")
    assert delete_response.status_code == 200

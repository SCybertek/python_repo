import json
from dataclasses import dataclass
from typing import Any, Optional
from urllib import error, parse, request
from uuid import uuid4

import pytest


BASE_URL = "https://petstore.swagger.io/v2"


@dataclass
class ApiResponse:
    status_code: int
    headers: dict[str, str]
    body: Any


class PetstoreClient:
    def request(
        self,
        method: str,
        path: str,
        *,
        json_body: Optional[Any] = None,
        params: Optional[dict[str, Any]] = None,
        form_body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> ApiResponse:
        url = f"{BASE_URL}{path}"
        if params:
            url = f"{url}?{parse.urlencode(params, doseq=True)}"

        request_headers = {"Accept": "application/json"}
        if headers:
            request_headers.update(headers)

        body = None
        if json_body is not None:
            body = json.dumps(json_body).encode("utf-8")
            request_headers["Content-Type"] = "application/json"
        elif form_body is not None:
            body = parse.urlencode(form_body).encode("utf-8")
            request_headers["Content-Type"] = "application/x-www-form-urlencoded"

        api_request = request.Request(
            url=url,
            data=body,
            headers=request_headers,
            method=method.upper(),
        )

        try:
            with request.urlopen(api_request, timeout=20) as api_response:
                return self._build_response(api_response.status, api_response.headers, api_response.read())
        except error.HTTPError as api_error:
            return self._build_response(api_error.code, api_error.headers, api_error.read())

    @staticmethod
    def _build_response(status_code: int, headers: Any, raw_body: bytes) -> ApiResponse:
        text_body = raw_body.decode("utf-8") if raw_body else ""
        content_type = headers.get("Content-Type", "")

        parsed_body: Any = text_body
        if text_body and "application/json" in content_type:
            parsed_body = json.loads(text_body)

        return ApiResponse(
            status_code=status_code,
            headers=dict(headers.items()),
            body=parsed_body,
        )


@pytest.fixture(scope="session")
def api_client() -> PetstoreClient:
    return PetstoreClient()


@pytest.fixture
def pet_payload() -> dict[str, Any]:
    pet_id = uuid4().int % 10_000_000_000
    return {
        "id": pet_id,
        "category": {"id": 1, "name": "pytest"},
        "name": f"pytest-pet-{pet_id}",
        "photoUrls": ["https://example.com/pet.png"],
        "tags": [{"id": 1, "name": "api"}],
        "status": "available",
    }


@pytest.fixture
def order_payload(pet_payload: dict[str, Any]) -> dict[str, Any]:
    order_id = uuid4().int % 10
    if order_id == 0:
        order_id = 1
    return {
        "id": order_id,
        "petId": pet_payload["id"],
        "quantity": 1,
        "shipDate": "2026-05-12T12:00:00.000Z",
        "status": "placed",
        "complete": True,
    }


@pytest.fixture
def user_payload() -> dict[str, Any]:
    suffix = uuid4().hex[:10]
    return {
        "id": uuid4().int % 10_000_000_000,
        "username": f"pytest_user_{suffix}",
        "firstName": "Pytest",
        "lastName": "Runner",
        "email": f"pytest_{suffix}@example.com",
        "password": "petstore-password",
        "phone": "555-0100",
        "userStatus": 1,
    }

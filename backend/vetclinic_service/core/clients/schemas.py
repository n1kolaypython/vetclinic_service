from pydantic import BaseModel
from typing import Optional
from uuid import UUID


class Base(BaseModel): ...


class BaseClient(BaseModel):
    full_name: str
    phone_number: str
    email: str | None = None


class CreateClientRequest(BaseClient):

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "full_name": "Olivia Reed",
                    "phone_number": "123-456-7890",
                    "email": "olivia.reed3241@example.com",
                }
            ],
        },
    }


class UpdateClientRequest(BaseClient):
    full_name: str | None = None
    phone_number: str | None = None
    email: str | None = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "full_name": "Olivia Roys",
                    "email": "olivia.roys3241@example.com",
                },
            ],
        },
    }


class ClientResponse(BaseClient):
    id: UUID

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "full_name": "Olivia Reed",
                    "phone_number": "123-456-7890",
                    "email": "olivia.reed3241@example.com",
                },
            ],
        }
    }

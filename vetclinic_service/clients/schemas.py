from pydantic import BaseModel
from typing import Optional
from uuid import UUID


class Base(BaseModel): ...


class BaseClient(BaseModel):
    full_name: str
    phone_number: str
    email: str | None = None


class CreateClientRequest(BaseClient): ...


class UpdateClientRequest(BaseClient):
    full_name: str | None = None
    phone_number: str | None = None
    email: str | None = None


class ClientResponse(BaseClient):
    id: UUID

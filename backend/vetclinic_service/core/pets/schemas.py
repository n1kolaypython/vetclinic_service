from pydantic import BaseModel
from typing import Optional
from uuid import UUID


class Base(BaseModel): ...


class BasePet(BaseModel):
    nickname: str | None
    species: str
    breed: str | None
    owner_id: UUID

class CreatePetRequest(BasePet): ...


class UpdatePetRequest(BasePet):
    nickname: str | None = None
    species: str | None = None
    breed: str | None = None
    owner_id: UUID | None = None


class PetResponse(BasePet):
    id: UUID

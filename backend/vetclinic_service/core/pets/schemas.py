from doctest import Example
from pydantic import BaseModel
from typing import Optional
from uuid import UUID


class Base(BaseModel): ...


class BasePet(BaseModel):
    nickname: str | None
    species: str
    breed: str | None
    owner_id: UUID | None


class CreatePetRequest(BasePet):

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "nickname": "Puppy",
                    "species": "Dog",
                    "breed": None,
                    "owner_id": None,
                },
            ],
        },
    }


class UpdatePetRequest(BasePet):
    nickname: str | None = None
    species: str | None = None
    breed: str | None = None
    owner_id: UUID | None = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "nickname": "Puppy",
                    "species": "Dog",
                    "breed": "Akita",
                    "owner_id": None,
                },
            ],
        },
    }


class PetResponse(BasePet):
    id: UUID

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": "fe8baa23-2529-6203-4a19-1c568e2adae3",
                    "nickname": "Puppy",
                    "species": "Dog",
                    "breed": "Akita",
                    "owner_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                },
            ],
        },
    }

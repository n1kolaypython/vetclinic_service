import re
from uuid import UUID
from .errors import (
    PetNotFound,
    PetCreateAbort,
    PetNotFoundOrDeleteAbort,
    PetNotFoundOrUpdateAbort,
)
from .schemas import PetResponse, CreatePetRequest, UpdatePetRequest
import asyncpg
from .repo import PetRepo


class PetService:

    def __init__(self, repo: PetRepo) -> None:
        self.repo = repo

    async def get_pet(self, id: UUID) -> PetResponse:
        record: asyncpg.Record = await self.repo.get_single(id)
        if record is None:
            raise PetNotFound
        return PetResponse(
            id=record["id"],
            nickname=record["nickname"],
            species=record["species"],
            breed=record["breed"],
            owner_id=record["owner_id"],
        )

    async def get_all_pets(self, limit: int, offset: int) -> list[PetResponse]:
        records = await self.repo.get_all(limit, offset)
        return [
            PetResponse(
                id=r["id"],
                nickname=r["nickname"],
                species=r["species"],
                breed=r["breed"],
                owner_id=r["owner_id"],
            )
            for r in records
        ]

    async def create_pet(self, data: CreatePetRequest) -> PetResponse:
        record = await self.repo.insert_one(
            data.nickname,
            data.species,
            data.breed,
            data.owner_id,
        )
        if record is None:
            raise PetCreateAbort
        return PetResponse(
            id=record["id"],
            nickname=record["nickname"],
            species=record["species"],
            breed=record["breed"],
            owner_id=record["owner_id"],
        )

    async def update_pet(self, id: UUID, data: UpdatePetRequest) -> PetResponse:
        record = await self.repo.update_one(
            id,
            **data.model_dump(),
        )
        if record is None:
            raise PetNotFoundOrUpdateAbort
        return PetResponse(
            id=record["id"],
            nickname=record["nickname"],
            species=record["species"],
            breed=record["breed"],
            owner_id=record["owner_id"],
        )

    async def delete_pet(self, id: UUID) -> PetResponse:
        record = await self.repo.delete_one(id)
        if record is None:
            raise PetNotFoundOrDeleteAbort
        return PetResponse(
            id=record["id"],
            nickname=record["nickname"],
            species=record["species"],
            breed=record["breed"],
            owner_id=record["owner_id"],
        )

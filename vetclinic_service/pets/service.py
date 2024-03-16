from uuid import UUID
from .schemas import PetResponse, CreatePetRequest, UpdatePetRequest
import asyncpg
from .repo import PetRepo 


class PetService:

    def __init__(self, repo: PetRepo) -> None:
        self.repo = repo

    async def get_pet(self, id: UUID) -> PetResponse:
        record: asyncpg.Record = await self.repo.get_single(id)
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
        record: asyncpg.Record = await self.repo.insert_one(
            data.nickname,
            data.species,
            data.breed,
            data.owner_id,
        )
        return PetResponse(
            id=record["id"],
            nickname=record["nickname"],
            species=record["species"],
            breed=record["breed"],
            owner_id=record["owner_id"],
        )

    async def update_pet(self, id: UUID, data: UpdatePetRequest) -> PetResponse:
        record: asyncpg.Record = await self.repo.update_one(
            id,
            **data.model_dump(),
        )
        return PetResponse(
            id=record["id"],
            nickname=record["nickname"],
            species=record["species"],
            breed=record["breed"],
            owner_id=record["owner_id"],
        )

    async def delete_pet(self, id: UUID) -> PetResponse:
        record: asyncpg.Record = await self.repo.delete_one(id)
        return PetResponse(
            id=record["id"],
            nickname=record["nickname"],
            species=record["species"],
            breed=record["breed"],
            owner_id=record["owner_id"],
        )

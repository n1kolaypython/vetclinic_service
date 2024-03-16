from uuid import UUID
from .schemas import ClientResponse, CreateClientRequest, UpdateClientRequest
import asyncpg
from .repo import ClientRepo


class ClientService:

    def __init__(self, repo: ClientRepo) -> None:
        self.repo = repo

    async def get_client(self, id: UUID) -> ClientResponse:
        record: asyncpg.Record = await self.repo.get_single(id)
        return ClientResponse(
            id=record["id"],
            full_name=record["full_name"],
            phone_number=record["phone_number"],
            email=record["email"],
        )

    async def get_all_clients(self, limit: int, offset: int) -> list[ClientResponse]:
        records = await self.repo.get_all(limit, offset)
        return [
            ClientResponse(
                id=r["id"],
                full_name=r["full_name"],
                phone_number=r["phone_number"],
                email=r["email"],
            )
            for r in records
        ]

    async def create_client(self, data: CreateClientRequest) -> ClientResponse:
        record: asyncpg.Record = await self.repo.insert_one(
            data.full_name,
            data.phone_number,
            data.email,
        )
        return ClientResponse(
            id=record["id"],
            full_name=record["full_name"],
            phone_number=record["phone_number"],
            email=record["email"],
        )

    async def update_client(
        self, id: UUID, data: UpdateClientRequest
    ) -> ClientResponse:
        record: asyncpg.Record = await self.repo.update_one(
            id,
            **data.model_dump(),
        )
        return ClientResponse(
            id=record["id"],
            full_name=record["full_name"],
            phone_number=record["phone_number"],
            email=record["email"],
        )

    async def delete_client(self, id: UUID) -> ClientResponse:
        record: asyncpg.Record = await self.repo.delete_one(id)
        return ClientResponse(
            id=record["id"],
            full_name=record["full_name"],
            phone_number=record["phone_number"],
            email=record["email"],
        )

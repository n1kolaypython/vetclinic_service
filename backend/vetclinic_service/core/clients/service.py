from uuid import UUID

from .errors import ClientCreateAbort, ClientNotFound, ClientNotFoundOrDeleteAbort, ClientNotFoundOrUpdateAbort
from .schemas import ClientResponse, CreateClientRequest, UpdateClientRequest
import asyncpg
from .repo import ClientRepo


class ClientService:

    def __init__(self, repo: ClientRepo) -> None:
        self.repo = repo

    async def get_client(self, id: UUID) -> ClientResponse:
        record: asyncpg.Record = await self.repo.get_single(id)
        if record is None:
            raise ClientNotFound 
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
        if record is None:
            raise ClientCreateAbort 
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
        if record is None:
            raise ClientNotFoundOrUpdateAbort
        return ClientResponse(
            id=record["id"],
            full_name=record["full_name"],
            phone_number=record["phone_number"],
            email=record["email"],
        )

    async def delete_client(self, id: UUID) -> ClientResponse:
        record: asyncpg.Record = await self.repo.delete_one(id)
        if record is None:
            raise ClientNotFoundOrDeleteAbort
        return ClientResponse(
            id=record["id"],
            full_name=record["full_name"],
            phone_number=record["phone_number"],
            email=record["email"],
        )

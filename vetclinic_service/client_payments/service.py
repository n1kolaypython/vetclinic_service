from uuid import UUID
from .schemas import (
    ClientPaymentResponse,
    CreateClientPaymentRequest,
    UpdateClientPaymentRequest,
)
import asyncpg
from .repo import ClientPaymentRepo


class ClientPaymentService:

    def __init__(self, repo: ClientPaymentRepo) -> None:
        self.repo = repo

    async def get_client_payment(self, id: UUID) -> ClientPaymentResponse:
        record: asyncpg.Record = await self.repo.get_single(id)
        return ClientPaymentResponse(
            id=record["id"],
            total=record["total"],
            created_at=record["created_at"],
            appointment_id=record["appointment_id"],
        )

    async def get_all_client_payments(
        self, limit: int, offset: int
    ) -> list[ClientPaymentResponse]:
        records = await self.repo.get_all(limit, offset)
        return [
            ClientPaymentResponse(
                id=r["id"],
                total=r["total"],
                created_at=r["created_at"],
                appointment_id=r["appointment_id"],
            )
            for r in records
        ]

    async def create_client_payment(self, data: CreateClientPaymentRequest) -> ClientPaymentResponse:
        record: asyncpg.Record = await self.repo.insert_one(
            data.appointment_id,
            data.total,
        )
        return ClientPaymentResponse(
            id=record["id"],
            total=record["total"],
            created_at=record["created_at"],
            appointment_id=record["appointment_id"],
        )

    async def update_client_payment(
        self, id: UUID, data: UpdateClientPaymentRequest
    ) -> ClientPaymentResponse:
        record: asyncpg.Record = await self.repo.update_one(
            id,
            **data.model_dump(),
        )
        return ClientPaymentResponse(
            id=record["id"],
            total=record["total"],
            created_at=record["created_at"],
            appointment_id=record["appointment_id"],
        )

    async def delete_client_payment(self, id: UUID) -> ClientPaymentResponse:
        record: asyncpg.Record = await self.repo.delete_one(id)
        return ClientPaymentResponse(
            id=record["id"],
            total=record["total"],
            created_at=record["created_at"],
            appointment_id=record["appointment_id"],
        )

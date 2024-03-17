from uuid import UUID
from .errors import (
    ClientPaymentCreateAbort,
    ClientPaymentNotFound,
    ClientPaymentNotFoundOrDeleteAbort,
    ClientPaymentNotFoundOrUpdateAbort,
)
from .schemas import (
    ClientPaymentResponse,
    CreateClientPaymentRequest,
    UpdateClientPaymentRequest,
)
import asyncpg
from .repo import ClientPaymentRepo


class ClientPaymentService:

    def __init__(
        self,
        repo: ClientPaymentRepo,
    ) -> None:
        self.repo = repo

    async def get_client_payment(
        self,
        id: UUID,
    ) -> ClientPaymentResponse:
        record = await self.repo.get_single(id)

        if record is None:
            raise ClientPaymentNotFound

        return ClientPaymentResponse(
            id=record["id"],
            total=record["total"],
            created_at=record["created_at"],
            appointment_id=record["appointment_id"],
            client_id=record["client_id"],
        )

    async def get_all_client_payments(
        self,
        limit: int,
        offset: int,
    ) -> list[ClientPaymentResponse]:
        records = await self.repo.get_all(limit, offset)
        return [
            ClientPaymentResponse(
                id=r["id"],
                total=r["total"],
                created_at=r["created_at"],
                appointment_id=r["appointment_id"],
                client_id=r["client_id"],
            )
            for r in records
        ]

    async def create_client_payment(
        self,
        data: CreateClientPaymentRequest,
    ) -> ClientPaymentResponse:
        record = await self.repo.insert_one(
            data.appointment_id,
            data.total,
        )

        if record is None:
            raise ClientPaymentCreateAbort

        return ClientPaymentResponse(
            id=record["id"],
            total=record["total"],
            created_at=record["created_at"],
            appointment_id=record["appointment_id"],
            client_id=record["client_id"],
        )

    async def update_client_payment(
        self,
        id: UUID,
        data: UpdateClientPaymentRequest,
    ) -> ClientPaymentResponse:
        record = await self.repo.update_one(
            id,
            **data.model_dump(),
        )

        if record is None:
            raise ClientPaymentNotFoundOrUpdateAbort

        return ClientPaymentResponse(
            id=record["id"],
            total=record["total"],
            created_at=record["created_at"],
            appointment_id=record["appointment_id"],
            client_id=record["client_id"],
        )

    async def delete_client_payment(self, id: UUID) -> ClientPaymentResponse:
        record: asyncpg.Record = await self.repo.delete_one(id)

        if record is None:
            raise ClientPaymentNotFoundOrDeleteAbort

        return ClientPaymentResponse(
            id=record["id"],
            total=record["total"],
            created_at=record["created_at"],
            appointment_id=record["appointment_id"],
            client_id=record["client_id"],
        )

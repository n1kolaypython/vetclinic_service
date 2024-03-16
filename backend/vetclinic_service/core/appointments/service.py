from uuid import UUID
from .schemas import (
    AppointmentResponse,
    CreateAppointmentRequest,
    UpdateAppointmentRequest,
)
import asyncpg
from .repo import AppointmentRepo


class AppointmentService:

    def __init__(self, repo: AppointmentRepo) -> None:
        self.repo = repo

    async def get_appointment(self, id: UUID) -> AppointmentResponse:
        record: asyncpg.Record = await self.repo.get_single(id)
        return AppointmentResponse(
            id=record["id"],
            start_time=record["start_time"],
            end_time=record["end_time"],
            cabinet=record["cabinet"],
            created_at=record["created_at"],
            client_id=record["client_id"],
            employee_id=record["employee_id"],
            pet_id=record["pet_id"],
        )

    async def get_all_appointments(self, limit: int, offset: int) -> list[AppointmentResponse]:
        records = await self.repo.get_all(limit, offset)
        return [
            AppointmentResponse(
                id=r["id"],
                start_time=r["start_time"],
                end_time=r["end_time"],
                cabinet=r["cabinet"],
                created_at=r["created_at"],
                client_id=r["client_id"],
                employee_id=r["employee_id"],
                pet_id=r["pet_id"],
            )
            for r in records
        ]

    async def create_appointment(self, data: CreateAppointmentRequest) -> AppointmentResponse:
        record: asyncpg.Record = await self.repo.insert_one(
            data.start_time,
            data.end_time,
            data.cabinet,
            data.client_id,
            data.employee_id,
            data.pet_id,
        )
        return AppointmentResponse(
            id=record["id"],
            start_time=record["start_time"],
            end_time=record["end_time"],
            cabinet=record["cabinet"],
            created_at=record["created_at"],
            client_id=record["client_id"],
            employee_id=record["employee_id"],
            pet_id=record["pet_id"],
        )

    async def update_appointment(self, id: UUID, data: UpdateAppointmentRequest) -> AppointmentResponse:
        record: asyncpg.Record = await self.repo.update_one(
            id,
            **data.model_dump(),
        )
        return AppointmentResponse(
            id=record["id"],
            start_time=record["start_time"],
            end_time=record["end_time"],
            cabinet=record["cabinet"],
            created_at=record["created_at"],
            client_id=record["client_id"],
            employee_id=record["employee_id"],
            pet_id=record["pet_id"],
        )

    async def delete_appointment(self, id: UUID) -> AppointmentResponse:
        record: asyncpg.Record = await self.repo.delete_one(id)
        return AppointmentResponse(
            id=record["id"],
            start_time=record["start_time"],
            end_time=record["end_time"],
            cabinet=record["cabinet"],
            created_at=record["created_at"],
            client_id=record["client_id"],
            employee_id=record["employee_id"],
            pet_id=record["pet_id"],
        )

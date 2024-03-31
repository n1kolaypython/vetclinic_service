from uuid import UUID
from .schemas import EmployeeResponse, CreateEmployeeRequest, UpdateEmployeeRequest
from .errors import (
    EmployeeNotFound,
    EmployeeCreateAbort,
    EmployeeNotFoundOrDeleteAbort,
    EmployeeNotFoundOrUpdateAbort,
)
import asyncpg
from .repo import EmployeeRepo


class EmployeeService:

    def __init__(
        self,
        repo: EmployeeRepo,
    ) -> None:
        self.repo = repo

    async def get_employee(
        self,
        id: UUID,
    ) -> EmployeeResponse | None:
        record: asyncpg.Record = await self.repo.get_single(id)
        if record is None:
            raise EmployeeNotFound
        return EmployeeResponse(
            id=record["id"],
            full_name=record["full_name"],
            phone_number=record["phone_number"],
            email=record["email"],
        )

    async def get_all_employees(
        self,
        limit: int,
        offset: int,
    ) -> list[EmployeeResponse]:
        records = await self.repo.get_all(limit, offset)
        return [
            EmployeeResponse(
                id=r["id"],
                full_name=r["full_name"],
                phone_number=r["phone_number"],
                email=r["email"],
            )
            for r in records
        ]

    async def create_employee(
        self,
        data: CreateEmployeeRequest,
    ) -> EmployeeResponse:
        record: asyncpg.Record | None = await self.repo.insert_one(
            data.full_name,
            data.phone_number,
            data.email,
        )
        if record is None:
            raise EmployeeCreateAbort
        return EmployeeResponse(
            id=record["id"],
            full_name=record["full_name"],
            phone_number=record["phone_number"],
            email=record["email"],
        )

    async def update_employee(
        self,
        id: UUID,
        data: UpdateEmployeeRequest,
    ) -> EmployeeResponse:
        record: asyncpg.Record | None = await self.repo.update_one(
            id,
            **data.model_dump(),
        )
        if record is None:
            raise EmployeeNotFoundOrUpdateAbort
        return EmployeeResponse(
            id=record["id"],
            full_name=record["full_name"],
            phone_number=record["phone_number"],
            email=record["email"],
        )

    async def delete_employee(
        self,
        id: UUID,
    ) -> EmployeeResponse:
        record: asyncpg.Record | None = await self.repo.delete_one(id)
        if record is None:
            raise EmployeeNotFoundOrDeleteAbort
        return EmployeeResponse(
            id=record["id"],
            full_name=record["full_name"],
            phone_number=record["phone_number"],
            email=record["email"],
        )

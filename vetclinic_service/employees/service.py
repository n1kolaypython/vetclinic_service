from uuid import UUID
from .schemas import EmployeeResponse, CreateEmployeeRequest, UpdateEmployeeRequest 
import asyncpg
from .repo import EmployeeRepo 


class EmployeeService:

    def __init__(self, repo: EmployeeRepo) -> None:
        self.repo = repo

    async def get_employee(self, id: UUID) -> EmployeeResponse:
        record: asyncpg.Record = await self.repo.get_single(id)
        return EmployeeResponse(
            id=record["id"],
            full_name=record["full_name"],
            phone_number=record["phone_number"],
            email=record["email"],
        )

    async def get_all_employees(self, limit: int, offset: int) -> list[EmployeeResponse]:
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

    async def create_employee(self, data: CreateEmployeeRequest) -> EmployeeResponse:
        record: asyncpg.Record = await self.repo.insert_one(
            data.full_name,
            data.phone_number,
            data.email,
        )
        return EmployeeResponse(
            id=record["id"],
            full_name=record["full_name"],
            phone_number=record["phone_number"],
            email=record["email"],
        )

    async def update_employee(
        self, id: UUID, data: UpdateEmployeeRequest 
    ) -> EmployeeResponse:
        record: asyncpg.Record = await self.repo.update_one(
            id,
            **data.model_dump(),
        )
        return EmployeeResponse(
            id=record["id"],
            full_name=record["full_name"],
            phone_number=record["phone_number"],
            email=record["email"],
        )

    async def delete_employee(self, id: UUID) -> EmployeeResponse:
        record: asyncpg.Record = await self.repo.delete_one(id)
        return EmployeeResponse(
            id=record["id"],
            full_name=record["full_name"],
            phone_number=record["phone_number"],
            email=record["email"],
        )

import asyncpg
from typing import Any
from uuid import UUID


class EmployeeRepo:

    def __init__(
        self,
        conn: asyncpg.Connection,
    ):
        self.conn = conn

    async def get_all(
        self,
        limit: int,
        offset: int,
    ) -> list[asyncpg.Record]:
        stmt = await self.conn.prepare(
            "SELECT * FROM employees ORDER BY full_name LIMIT $1 OFFSET $2"
        )
        records: list[asyncpg.Record] = await stmt.fetch(limit, offset)
        return records

    async def get_single(
        self,
        id: UUID,
    ) -> asyncpg.Record:
        stmt = await self.conn.prepare("SELECT * FROM employees WHERE employees.id = $1")
        record: asyncpg.Record = await stmt.fetchrow(id)
        return record

    async def insert_one(
        self,
        full_name: str,
        phone_number: str,
        email: str | None,
    ) -> asyncpg.Record:
        record: asyncpg.Record
        async with self.conn.transaction():
            record = await self.conn.fetchrow(
                "INSERT INTO employees (full_name, phone_number, email) VALUES ($1, $2, $3) RETURNING *",
                full_name,
                phone_number,
                email,
            )

        return record

    async def update_one(
        self,
        id: UUID,
        **data: dict[str, Any],
    ) -> asyncpg.Record | None:
        record: asyncpg.Record | None
        set_stmt = ", ".join(
            [
                f"{key} = ${idx}"
                for idx, key in enumerate(
                    [key for key in data.keys() if data[key] != None],
                    start=2,
                )
            ]
        )
        async with self.conn.transaction():
            record = await self.conn.fetchrow(
                f"UPDATE employees SET {set_stmt} WHERE employees.id = $1 RETURNING *",
                id,
                *[value for value in data.values() if value is not None],
            )

        return record

    async def delete_one(
        self,
        id: UUID,
    ) -> asyncpg.Record:
        record: asyncpg.Record
        async with self.conn.transaction():
            record = await self.conn.fetchrow(
                "DELETE FROM employees WHERE employees.id = $1 RETURNING *", id
            )

        return record

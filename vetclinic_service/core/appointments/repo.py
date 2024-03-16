import asyncpg
from datetime import datetime
from typing import Any
from uuid import UUID


class AppointmentRepo:

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
        stmt = await self.conn.prepare("SELECT * FROM appointments LIMIT $1 OFFSET $2")
        records: list[asyncpg.Record] = await stmt.fetch(limit, offset)
        return records

    async def get_between(
        self,
    ) -> list[asyncpg.Record]: ...

    async def get_single(
        self,
        id: UUID,
    ) -> asyncpg.Record:
        stmt = await self.conn.prepare(
            "SELECT * FROM appointments WHERE appointments.id = $1"
        )
        record: asyncpg.Record = await stmt.fetchrow(str(id))
        return record

    async def insert_one(
        self,
        start_time: datetime,
        end_time: datetime,
        cabinet: str,
        client_id: UUID,
        employee_id: UUID,
        pet_id: UUID,
    ) -> asyncpg.Record:
        record: asyncpg.Record
        async with self.conn.transaction():
            record = await self.conn.fetchrow(
                "INSERT INTO appointments (start_time, end_time, cabinet, client_id, employee_id, pet_id) VALUES ($1, $2, $3, $4, $5, $6) RETURNING *",
                start_time,
                end_time,
                cabinet,
                str(client_id),
                str(employee_id),
                str(pet_id),
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
                f"UPDATE appointments SET {set_stmt} WHERE appointments.id = $1 RETURNING *",
                str(id),
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
                "DELETE FROM appointments WHERE appointments.id = $1 RETURNING *", str(id)
            )

        return record

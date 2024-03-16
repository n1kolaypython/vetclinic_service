from decimal import Decimal
import asyncpg
from datetime import datetime
from typing import Any
from uuid import UUID


class ClientPaymentRepo:

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
        stmt = await self.conn.prepare("SELECT * FROM client_payments LIMIT $1 OFFSET $2")
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
            "SELECT * FROM client_payments WHERE client_payments.id = $1"
        )
        record: asyncpg.Record = await stmt.fetchrow(str(id))
        return record

    async def insert_one(
        self,
        appointmend_id: UUID,
        total: Decimal 
    ) -> asyncpg.Record:
        record: asyncpg.Record
        async with self.conn.transaction():
            record = await self.conn.fetchrow(
                "INSERT INTO client_payments (total, appointment_id) VALUES ($1, $2) RETURNING *",
                total,
                str(appointmend_id),
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
                f"UPDATE client_payments SET {set_stmt} WHERE client_payments.id = $1 RETURNING *",
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
                "DELETE FROM client_payments WHERE client_payments.id = $1 RETURNING *", str(id)
            )

        return record

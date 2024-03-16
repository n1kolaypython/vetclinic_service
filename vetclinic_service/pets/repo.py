import asyncpg
from typing import Any
from uuid import UUID


class PetRepo:

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
        stmt = await self.conn.prepare("SELECT * FROM pets LIMIT $1 OFFSET $2")
        records: list[asyncpg.Record] = await stmt.fetch(limit, offset)
        return records

    async def get_single(
        self,
        id: UUID,
    ) -> asyncpg.Record:
        stmt = await self.conn.prepare("SELECT * FROM pets WHERE pets.id = $1")
        record: asyncpg.Record = await stmt.fetchrow(id)
        return record

    async def insert_one(
        self,
        nickname: str,
        species: str,
        breed: str,
        owner_id: UUID,
    ) -> asyncpg.Record:
        record: asyncpg.Record
        async with self.conn.transaction():
            record = await self.conn.fetchrow(
                "INSERT INTO pets (nickname, species, breed, owner_id) VALUES ($1, $2, $3, $4) RETURNING *",
                nickname,
                species,
                breed,
                owner_id,
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
                f"UPDATE pets SET {set_stmt} WHERE pets.id = $1 RETURNING *",
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
                "DELETE FROM pets WHERE pets.id = $1 RETURNING *", id
            )

        return record

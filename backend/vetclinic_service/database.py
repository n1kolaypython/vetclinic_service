import asyncpg
from typing import AsyncGenerator
from vetclinic_service.config import DatabaseConfig

cfg = DatabaseConfig()


async def get_db_conn() -> AsyncGenerator[asyncpg.Connection, None]:
    conn = await asyncpg.connect(
        user=cfg.user,
        password=cfg.password,
        host=cfg.host,
        port=cfg.port,
        database=cfg.name,
    )
    try:
        yield conn
    finally:
        await conn.close()

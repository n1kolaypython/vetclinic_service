from fastapi import Depends
from .repo import ClientRepo
from .service import ClientService
from typing import Annotated
from vetclinic_service.database import get_db_conn
import asyncpg


async def get_client_repo(
    conn: Annotated[asyncpg.Connection, Depends(get_db_conn)]
) -> ClientRepo:
    return ClientRepo(conn)


async def get_client_service(
    repo: Annotated[ClientRepo, Depends(get_client_repo)]
) -> ClientService:
    return ClientService(repo)

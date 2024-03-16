from fastapi import Depends
from .repo import ClientPaymentRepo 
from .service import ClientPaymentService 
from typing import Annotated
from vetclinic_service.database import get_db_conn
import asyncpg


async def get_appointment_repo(
    conn: Annotated[asyncpg.Connection, Depends(get_db_conn)]
) -> ClientPaymentRepo:
    return ClientPaymentRepo(conn)


async def get_appointment_service(
    repo: Annotated[ClientPaymentRepo, Depends(get_appointment_repo)]
) -> ClientPaymentService:
    return ClientPaymentService(repo)

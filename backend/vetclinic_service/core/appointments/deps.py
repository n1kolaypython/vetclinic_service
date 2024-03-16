from fastapi import Depends
from .repo import AppointmentRepo 
from .service import AppointmentService 
from typing import Annotated
from vetclinic_service.database import get_db_conn
import asyncpg


async def get_appointment_repo(
    conn: Annotated[asyncpg.Connection, Depends(get_db_conn)]
) -> AppointmentRepo:
    return AppointmentRepo(conn)


async def get_appointment_service(
    repo: Annotated[AppointmentRepo, Depends(get_appointment_repo)]
) -> AppointmentService:
    return AppointmentService(repo)

from fastapi import Depends
from .repo import EmployeeRepo 
from .service import EmployeeService 
from typing import Annotated
from vetclinic_service.database import get_db_conn
import asyncpg


async def get_employee_repo(
    conn: Annotated[asyncpg.Connection, Depends(get_db_conn)]
) -> EmployeeRepo:
    return EmployeeRepo(conn)


async def get_employee_service(
    repo: Annotated[EmployeeRepo, Depends(get_employee_repo)]
) -> EmployeeService:
    return EmployeeService(repo)

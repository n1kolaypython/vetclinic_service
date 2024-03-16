from fastapi import Depends
from .repo import PetRepo 
from .service import PetService 
from typing import Annotated
from vetclinic_service.database import get_db_conn
import asyncpg


async def get_pet_repo(
    conn: Annotated[asyncpg.Connection, Depends(get_db_conn)]
) -> PetRepo:
    return PetRepo(conn)


async def get_pet_service(
    repo: Annotated[PetRepo, Depends(get_pet_repo)]
) -> PetService:
    return PetService(repo)

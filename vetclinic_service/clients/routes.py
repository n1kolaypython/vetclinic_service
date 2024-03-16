from fastapi import APIRouter, status, Depends
from uuid import UUID
from typing import Annotated
from .schemas import CreateClientRequest, ClientResponse, UpdateClientRequest
from .service import ClientService
from .deps import get_client_service

router = APIRouter(prefix="/clients", tags=["clients"])


@router.get("/", status_code=status.HTTP_200_OK)
async def get_clients(
    service: Annotated[ClientService, Depends(get_client_service)],
    limit: int = 10,
    offset: int = 0,
) -> list[ClientResponse]:
    return await service.get_all_clients(limit, offset)


@router.get("/{id}", status_code=status.HTTP_200_OK)
async def get_one_client(
    service: Annotated[ClientService, Depends(get_client_service)],
    id: UUID,
) -> ClientResponse:
    return await service.get_client(id)

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_new_client(
    service: Annotated[ClientService, Depends(get_client_service)],
    data: CreateClientRequest,
) -> ClientResponse:
    return await service.create_client(data)

@router.patch("/{id}", status_code=status.HTTP_200_OK)
async def update_client(
    service: Annotated[ClientService, Depends(get_client_service)],
    id: UUID,
    data: UpdateClientRequest,
) -> ClientResponse:
    return await service.update_client(id, data)

@router.delete("/{id}", status_code=status.HTTP_200_OK)
async def delete_client(
    service: Annotated[ClientService, Depends(get_client_service)],
    id: UUID,
) -> ClientResponse:
    return await service.delete_client(id)

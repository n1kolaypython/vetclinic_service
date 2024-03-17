from fastapi import APIRouter, status, Depends, HTTPException
from uuid import UUID
from typing import Annotated
from .schemas import CreateClientRequest, ClientResponse, UpdateClientRequest
from .errors import (
    ClientNotFound,
    ClientNotFoundOrDeleteAbort,
    ClientNotFoundOrUpdateAbort,
    ClientCreateAbort,
)
from .service import ClientService
from .deps import get_client_service

router = APIRouter()


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
) -> ClientResponse | None:
    try:
        return await service.get_client(id)
    except ClientNotFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="client not found",
        )


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_new_client(
    service: Annotated[ClientService, Depends(get_client_service)],
    data: CreateClientRequest,
) -> ClientResponse | None:
    try:
        return await service.create_client(data)
    except ClientCreateAbort:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="failed to create client",
        )


@router.patch("/{id}", status_code=status.HTTP_200_OK)
async def update_client(
    service: Annotated[ClientService, Depends(get_client_service)],
    id: UUID,
    data: UpdateClientRequest,
) -> ClientResponse | None:
    try:
        return await service.update_client(id, data)
    except ClientNotFoundOrUpdateAbort:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="client not found or client update was failed",
        )


@router.delete("/{id}", status_code=status.HTTP_200_OK)
async def delete_client(
    service: Annotated[ClientService, Depends(get_client_service)],
    id: UUID,
) -> ClientResponse | None:
    try:
        return await service.delete_client(id)
    except ClientNotFoundOrDeleteAbort:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="client not found or client delete was failed",
        )

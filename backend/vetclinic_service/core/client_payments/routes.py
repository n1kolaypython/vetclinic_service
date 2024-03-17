from email.policy import HTTP
from fastapi import APIRouter, status, Depends, HTTPException
from uuid import UUID
from typing import Annotated
from .errors import (
    ClientPaymentNotFoundOrUpdateAbort,
    ClientPaymentCreateAbort,
    ClientPaymentNotFound,
    ClientPaymentNotFoundOrDeleteAbort,
)
from .schemas import (
    ClientPaymentResponse,
    CreateClientPaymentRequest,
    UpdateClientPaymentRequest,
)
from .service import ClientPaymentService
from .deps import get_appointment_service

router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK)
async def get_client_payments(
    service: Annotated[ClientPaymentService, Depends(get_appointment_service)],
    limit: int = 10,
    offset: int = 0,
) -> list[ClientPaymentResponse]:
    return await service.get_all_client_payments(limit, offset)


@router.get("/{id}", status_code=status.HTTP_200_OK)
async def get_one_client_payment(
    service: Annotated[ClientPaymentService, Depends(get_appointment_service)],
    id: UUID,
) -> ClientPaymentResponse:
    try:
        return await service.get_client_payment(id)
    except ClientPaymentNotFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="client payment not found",
        )


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_new_client_payment(
    service: Annotated[ClientPaymentService, Depends(get_appointment_service)],
    data: CreateClientPaymentRequest,
) -> ClientPaymentResponse:
    try:
        return await service.create_client_payment(data)
    except ClientPaymentCreateAbort:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="failed to create client payment",
        )


@router.patch("/{id}", status_code=status.HTTP_200_OK)
async def update_client_payment(
    service: Annotated[ClientPaymentService, Depends(get_appointment_service)],
    id: UUID,
    data: UpdateClientPaymentRequest,
) -> ClientPaymentResponse:
    try:
        return await service.update_client_payment(id, data)
    except ClientPaymentNotFoundOrUpdateAbort:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="client payment not found or client payment update was failed",
        )


@router.delete("/{id}", status_code=status.HTTP_200_OK)
async def delete_client_payment(
    service: Annotated[ClientPaymentService, Depends(get_appointment_service)],
    id: UUID,
) -> ClientPaymentResponse:
    try:
        return await service.delete_client_payment(id)
    except ClientPaymentNotFoundOrDeleteAbort:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="client payment not found or client payment create was failed",
        )
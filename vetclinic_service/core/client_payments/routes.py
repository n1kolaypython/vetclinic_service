from fastapi import APIRouter, status, Depends
from uuid import UUID
from typing import Annotated
from .schemas import ClientPaymentResponse, CreateClientPaymentRequest, UpdateClientPaymentRequest 
from .service import ClientPaymentService 
from .deps import get_appointment_service 

router = APIRouter(prefix="/payments", tags=["clients"])


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
    return await service.get_client_payment(id)

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_new_client_payment(
    service: Annotated[ClientPaymentService, Depends(get_appointment_service)],
    data: CreateClientPaymentRequest,
) -> ClientPaymentResponse:
    return await service.create_client_payment(data)

@router.patch("/{id}", status_code=status.HTTP_200_OK)
async def update_client_payment(
    service: Annotated[ClientPaymentService, Depends(get_appointment_service)],
    id: UUID,
    data: UpdateClientPaymentRequest,
) -> ClientPaymentResponse:
    return await service.update_client_payment(id, data)

@router.delete("/{id}", status_code=status.HTTP_200_OK)
async def delete_client_payment(
    service: Annotated[ClientPaymentService, Depends(get_appointment_service)],
    id: UUID,
) -> ClientPaymentResponse:
    return await service.delete_client_payment(id)

from fastapi import APIRouter, status, Depends, HTTPException
from uuid import UUID
from typing import Annotated
from .schemas import (
    CreateAppointmentRequest,
    UpdateAppointmentRequest,
    AppointmentResponse,
)
from .errors import (
    AppointmentNotFoundOrDeleteAbort,
    AppointmentCreateAbort,
    AppointmentNotFound,
    AppointmentNotFoundOrUpdateAbort,
)
from .service import AppointmentService
from .deps import get_appointment_service

router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK)
async def get_appointments(
    service: Annotated[AppointmentService, Depends(get_appointment_service)],
    limit: int = 10,
    offset: int = 0,
) -> list[AppointmentResponse]:
    return await service.get_all_appointments(limit, offset)


@router.get("/{id}", status_code=status.HTTP_200_OK)
async def get_one_appointment(
    service: Annotated[AppointmentService, Depends(get_appointment_service)],
    id: UUID,
) -> AppointmentResponse | None:
    try:
        return await service.get_appointment(id)
    except AppointmentNotFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="appointment not found",
        )


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_new_appointment(
    service: Annotated[AppointmentService, Depends(get_appointment_service)],
    data: CreateAppointmentRequest,
) -> AppointmentResponse:
    try:
        return await service.create_appointment(data)
    except AppointmentCreateAbort:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="failed to create appointment",
        )


@router.patch("/{id}", status_code=status.HTTP_200_OK)
async def update_appointment(
    service: Annotated[AppointmentService, Depends(get_appointment_service)],
    id: UUID,
    data: UpdateAppointmentRequest,
) -> AppointmentResponse:
    try:
        return await service.update_appointment(id, data)
    except AppointmentNotFoundOrUpdateAbort:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="appointment not found or appointment update was failed",
        )


@router.delete("/{id}", status_code=status.HTTP_200_OK)
async def delete_appointment(
    service: Annotated[AppointmentService, Depends(get_appointment_service)],
    id: UUID,
) -> AppointmentResponse:
    try:
        return await service.delete_appointment(id)
    except AppointmentNotFoundOrDeleteAbort:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="appointment not found or appointment delete was failed",
        )

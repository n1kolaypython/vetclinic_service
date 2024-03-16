from fastapi import APIRouter, status, Depends
from uuid import UUID
from typing import Annotated
from .schemas import CreateAppointmentRequest, UpdateAppointmentRequest, AppointmentResponse 
from .service import AppointmentService 
from .deps import get_appointment_service 

router = APIRouter(prefix="/appointments", tags=["appointments"])


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
) -> AppointmentResponse:
    return await service.get_appointment(id)

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_new_client(
    service: Annotated[AppointmentService, Depends(get_appointment_service)],
    data: CreateAppointmentRequest,
) -> AppointmentResponse:
    return await service.create_appointment(data)

@router.patch("/{id}", status_code=status.HTTP_200_OK)
async def update_client(
    service: Annotated[AppointmentService, Depends(get_appointment_service)],
    id: UUID,
    data: UpdateAppointmentRequest,
) -> AppointmentResponse:
    return await service.update_appointment(id, data)

@router.delete("/{id}", status_code=status.HTTP_200_OK)
async def delete_client(
    service: Annotated[AppointmentService, Depends(get_appointment_service)],
    id: UUID,
) -> AppointmentResponse:
    return await service.delete_appointment(id)

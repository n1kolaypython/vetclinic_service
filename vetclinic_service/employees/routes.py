from fastapi import APIRouter, status, Depends
from uuid import UUID
from typing import Annotated
from .schemas import EmployeeResponse, CreateEmployeeRequest, UpdateEmployeeRequest 
from .service import EmployeeService 
from .deps import get_employee_service 

router = APIRouter(prefix="/employee", tags=["employees"])


@router.get("/", status_code=status.HTTP_200_OK)
async def get_employees(
    service: Annotated[EmployeeService, Depends(get_employee_service)],
    limit: int = 10,
    offset: int = 0,
) -> list[EmployeeResponse]:
    return await service.get_all_employees(limit, offset)


@router.get("/{id}", status_code=status.HTTP_200_OK)
async def get_one_employee(
    service: Annotated[EmployeeService, Depends(get_employee_service)],
    id: UUID,
) -> EmployeeResponse:
    return await service.get_employee(id)

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_new_employee(
    service: Annotated[EmployeeService, Depends(get_employee_service)],
    data: CreateEmployeeRequest,
) -> EmployeeResponse:
    return await service.create_employee(data)

@router.patch("/{id}", status_code=status.HTTP_200_OK)
async def update_employee(
    service: Annotated[EmployeeService, Depends(get_employee_service)],
    id: UUID,
    data: UpdateEmployeeRequest,
) -> EmployeeResponse:
    return await service.update_employee(id, data)

@router.delete("/{id}", status_code=status.HTTP_200_OK)
async def delete_employee(
    service: Annotated[EmployeeService, Depends(get_employee_service)],
    id: UUID,
) -> EmployeeResponse:
    return await service.delete_employee(id)

from fastapi import APIRouter, status, Depends, HTTPException
from uuid import UUID
from typing import Annotated
from .errors import (
    EmployeeNotFound,
    EmployeeCreateAbort,
    EmployeeNotFoundOrUpdateAbort,
    EmployeeNotFoundOrDeleteAbort,
)
from .schemas import EmployeeResponse, CreateEmployeeRequest, UpdateEmployeeRequest
from .service import EmployeeService
from .deps import get_employee_service

router = APIRouter()


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
) -> EmployeeResponse | None:
    try:
        return await service.get_employee(id)
    except EmployeeNotFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="employee not found",
        )


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_new_employee(
    service: Annotated[EmployeeService, Depends(get_employee_service)],
    data: CreateEmployeeRequest,
) -> EmployeeResponse | None:
    try:
        return await service.create_employee(data)
    except EmployeeCreateAbort:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="failed to create employee",
        )


@router.patch("/{id}", status_code=status.HTTP_200_OK)
async def update_employee(
    service: Annotated[EmployeeService, Depends(get_employee_service)],
    id: UUID,
    data: UpdateEmployeeRequest,
) -> EmployeeResponse | None:
    try:
        return await service.update_employee(id, data)
    except EmployeeNotFoundOrUpdateAbort:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="employee not found or employee update was failed",
        )


@router.delete("/{id}", status_code=status.HTTP_200_OK)
async def delete_employee(
    service: Annotated[EmployeeService, Depends(get_employee_service)],
    id: UUID,
) -> EmployeeResponse:
    try:
        return await service.delete_employee(id)
    except EmployeeNotFoundOrDeleteAbort:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="employee not found or employee create was failed",
        )

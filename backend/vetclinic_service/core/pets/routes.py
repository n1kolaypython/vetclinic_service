from fastapi import APIRouter, status, Depends, HTTPException
from uuid import UUID
from typing import Annotated
from .schemas import CreatePetRequest, UpdatePetRequest, PetResponse
from .errors import (
    PetNotFoundOrDeleteAbort,
    PetCreateAbort,
    PetNotFound,
    PetNotFoundOrUpdateAbort,
)
from .service import PetService
from .deps import get_pet_service

router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK)
async def get_all_pets(
    service: Annotated[PetService, Depends(get_pet_service)],
    limit: int = 10,
    offset: int = 0,
) -> list[PetResponse]:
    return await service.get_all_pets(limit, offset)


@router.get("/{id}", status_code=status.HTTP_200_OK)
async def get_one_pet(
    service: Annotated[PetService, Depends(get_pet_service)],
    id: UUID,
) -> PetResponse | None:
    try:
        return await service.get_pet(id)
    except PetNotFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="pet not found",
        )


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_new_pet(
    service: Annotated[PetService, Depends(get_pet_service)],
    data: CreatePetRequest,
) -> PetResponse | None:
    try:
        return await service.create_pet(data)
    except PetCreateAbort:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="failed to create pet"
        )


@router.patch("/{id}", status_code=status.HTTP_200_OK)
async def update_pet(
    service: Annotated[PetService, Depends(get_pet_service)],
    id: UUID,
    data: UpdatePetRequest,
) -> PetResponse | None:
    try:
        return await service.update_pet(id, data)
    except PetNotFoundOrUpdateAbort:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="pet not found or pet update was failed",
        )


@router.delete("/{id}", status_code=status.HTTP_200_OK)
async def delete_pet(
    service: Annotated[PetService, Depends(get_pet_service)],
    id: UUID,
) -> PetResponse | None:
    try:
        return await service.delete_pet(id)
    except PetNotFoundOrDeleteAbort:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="pet not found or delete pet was failed",
        )

from fastapi import APIRouter, status, Depends
from uuid import UUID
from typing import Annotated
from .schemas import CreatePetRequest, UpdatePetRequest, PetResponse 
from .service import PetService 
from .deps import get_pet_service

router = APIRouter(prefix="/pets", tags=["pets"])


@router.get("/", status_code=status.HTTP_200_OK)
async def get_pets(
    service: Annotated[PetService, Depends(get_pet_service)],
    limit: int = 10,
    offset: int = 0,
) -> list[PetResponse]:
    return await service.get_all_pets(limit, offset)


@router.get("/{id}", status_code=status.HTTP_200_OK)
async def get_one_client(
    service: Annotated[PetService, Depends(get_pet_service)],
    id: UUID,
) -> PetResponse:
    return await service.get_pet(id)

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_new_client(
    service: Annotated[PetService, Depends(get_pet_service)],
    data: CreatePetRequest,
) -> PetResponse:
    return await service.create_pet(data)

@router.patch("/{id}", status_code=status.HTTP_200_OK)
async def update_client(
    service: Annotated[PetService, Depends(get_pet_service)],
    id: UUID,
    data: UpdatePetRequest,
) -> PetResponse:
    return await service.update_pet(id, data)

@router.delete("/{id}", status_code=status.HTTP_200_OK)
async def delete_client(
    service: Annotated[PetService, Depends(get_pet_service)],
    id: UUID,
) -> PetResponse:
    return await service.delete_pet(id)

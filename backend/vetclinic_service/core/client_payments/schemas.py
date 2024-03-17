from decimal import Decimal
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from uuid import UUID


class Base(BaseModel): ...


class BaseClientPayment(BaseModel):

    total: Decimal
    client_id: UUID
    appointment_id: UUID


class CreateClientPaymentRequest(BaseClientPayment):

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "client_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "appointment_id": "b4b385a6-f2e4-c3c4-542d-ae18ed04e9c6",
                    "total": 1200.50,
                },
            ],
        },
    }


class UpdateClientPaymentRequest(BaseClientPayment):

    total: Decimal | None = None
    appointment_id: UUID | None = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "client_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "appointment_id": "b4b385a6-f2e4-c3c4-542d-ae18ed04e9c6",
                    "total": 1200.50,
                },
            ],
        },
    }


class ClientPaymentResponse(BaseClientPayment):

    id: UUID
    created_at: datetime

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": "3fa85f64-5717-4562-b3fc-2c963f66afb6",
                    "client_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "appointment_id": "b4b385a6-f2e4-c3c4-542d-ae18ed04e9c6",
                    "total": 1200.50,
                },
            ],
        },
    }

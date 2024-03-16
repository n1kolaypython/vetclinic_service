from decimal import Decimal
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from uuid import UUID


class Base(BaseModel): ...


class BaseClientPayment(BaseModel):

    total: Decimal
    appointment_id: UUID
    created_at: datetime 

class CreateClientPaymentRequest(BaseClientPayment): ...


class UpdateClientPaymentRequest(BaseClientPayment):

    total: Decimal | None = None
    appointment_id: UUID | None = None

class ClientPaymentResponse(BaseClientPayment):

    id: UUID
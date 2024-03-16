from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from uuid import UUID


class Base(BaseModel): ...


class BaseAppointment(BaseModel):
    start_time: datetime
    end_time: datetime
    cabinet: str
    created_at: datetime

    client_id: UUID
    employee_id: UUID
    pet_id: UUID

class CreateAppointmentRequest(BaseAppointment): ...


class UpdateAppointmentRequest(BaseAppointment):
    start_time: datetime | None = None
    end_time: datetime | None = None
    cabinet: str | None = None
    created_at: datetime | None = None

    client_id: UUID | None = None
    employee_id: UUID | None = None
    pet_id: UUID | None = None


class AppointmentResponse(BaseAppointment):

    id: UUID
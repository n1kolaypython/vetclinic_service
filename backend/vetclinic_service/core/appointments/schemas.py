from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from uuid import UUID


class Base(BaseModel): ...


class BaseAppointment(BaseModel):
    start_time: datetime
    end_time: datetime
    cabinet: str

    client_id: UUID | None
    employee_id: UUID
    pet_id: UUID | None

class CreateAppointmentRequest(BaseAppointment): 

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "start_time": "2023-02-27T13:00:00",
                    "end_time": "2023-02-27T14:00:00",
                    "cabinet": "A-101",
                    "client_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "employee_id": "b4b385a6-f2e4-c3c4-542d-ae18ed04e9c6",
                    "pet_id": "fe8baa23-2529-6203-4a19-1c568e2adae",
                },
            ],
        },
    }



class UpdateAppointmentRequest(BaseAppointment):
    start_time: datetime | None = None
    end_time: datetime | None = None
    cabinet: str | None = None

    client_id: UUID | None = None
    employee_id: UUID | None = None
    pet_id: UUID | None = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "start_time": "2023-02-27T13:00:00",
                    "end_time": "2023-02-27T14:00:00",
                    "cabinet": "A-101",
                    "client_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "employee_id": "b4b385a6-f2e4-c3c4-542d-ae18ed04e9c6",
                    "pet_id": "fe8baa23-2529-6203-4a19-1c568e2adae",
                },
            ],
        },
    }


class AppointmentResponse(BaseAppointment):

    id: UUID
    created_at: datetime

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "start_time": "2023-02-27T13:00:00",
                    "end_time": "2023-02-27T14:00:00",
                    "cabinet": "A-101",
                    "client_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "employee_id": "b4b385a6-f2e4-c3c4-542d-ae18ed04e9c6",
                    "pet_id": "fe8baa23-2529-6203-4a19-1c568e2adae",
                    "created_at": "2023-02-26T14:20:00",
                },
            ],
        },
    }
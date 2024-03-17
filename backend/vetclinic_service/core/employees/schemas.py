from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from uuid import UUID


class Base(BaseModel): ...


class BaseEmployee(BaseModel):
    full_name: str
    phone_number: str
    email: str


class CreateEmployeeRequest(BaseEmployee):

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "full_name": "Jason Statham",
                    "phone_number": "999-999-9999",
                    "email": "jason.statham228@example.com",
                }
            ]
        }
    }


class UpdateEmployeeRequest(BaseEmployee):
    full_name: str | None = None
    phone_number: str | None = None
    email: str | None = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "full_name": "Jason STATHAM",
                    "phone_number": "111-222-3333",
                    "email": "jason.statham999@example.com",
                }
            ]
        }
    }


class EmployeeResponse(BaseEmployee):
    id: UUID

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": "2b448d19-d40b-a05b-ca96-4c63a30374c7",
                    "full_name": "Jason Statham",
                    "phone_number": "999-999-9999",
                    "email": "jason.statham228@example.com",
                },
            ]
        }
    }

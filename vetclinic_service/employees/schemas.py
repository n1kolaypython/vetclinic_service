from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from uuid import UUID


class Base(BaseModel): ...


class BaseEmployee(BaseModel):
    full_name: str
    phone_number: str
    email: str | None = None

class CreateEmployeeRequest(BaseEmployee): ...


class UpdateEmployeeRequest(BaseEmployee):
    full_name: str | None = None
    phone_number: str | None = None
    email: str | None = None


class EmployeeResponse(BaseEmployee):
    id: UUID

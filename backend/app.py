from fastapi import FastAPI
from vetclinic_service.core.clients.routes import router as client_router
from vetclinic_service.core.pets.routes import router as pet_router
from vetclinic_service.core.employees.routes import router as employee_router
from vetclinic_service.core.appointments.routes import router as appointment_router
from vetclinic_service.core.client_payments.routes import (
    router as client_payment_router,
)

app = FastAPI()
app.include_router(
    client_router,
    prefix="/client",
    tags=["client"],
)
app.include_router(
    pet_router,
    prefix="/pet",
    tags=["pet"],
)
app.include_router(
    employee_router,
    prefix="/employee",
    tags=["employee"],
)
app.include_router(
    appointment_router,
    prefix="/appointment",
    tags=["appointment"],
)
app.include_router(
    client_payment_router,
    prefix="/payment",
    tags=["client"],
)

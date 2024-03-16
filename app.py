from fastapi import FastAPI
from vetclinic_service.core.clients.routes import router as client_router
from vetclinic_service.core.pets.routes import router as pet_router
from vetclinic_service.core.employees.routes import router as employee_router
from vetclinic_service.core.appointments.routes import router as appointment_router
from vetclinic_service.core.client_payments.routes import router as client_payment_router

app = FastAPI()
app.include_router(client_router)
app.include_router(pet_router)
app.include_router(employee_router)
app.include_router(appointment_router)
app.include_router(client_payment_router)

from fastapi import FastAPI
from vetclinic_service.clients.routes import router as client_router
from vetclinic_service.pets.routes import router as pet_router
from vetclinic_service.employees.routes import router as employee_router

app = FastAPI()
app.include_router(client_router)
app.include_router(pet_router)
app.include_router(employee_router)
from fastapi import FastAPI
from src.router.CompanyRouter import router as company_router
from src.router.EmployeeRouter import router as employee_router

app = FastAPI(title="FastAPI + MongoDB CRUD with UUID")

app.include_router(company_router)
app.include_router(employee_router)

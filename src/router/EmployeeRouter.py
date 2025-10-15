from fastapi import APIRouter, HTTPException
from src.repo.EmployeeRepo import EmployeeRepo
from src.models.EmployeeModel import EmployeeModel
from src.request.EmployeeRequest import EmployeeRequest

router = APIRouter(prefix="/employees", tags=["Employees"])

@router.post("/")
async def create_employee(req: EmployeeRequest):
    employee = EmployeeModel(
        employee_name=req.employee_name,
        employee_company=req.employee_company  # company_id
    )
    return await EmployeeRepo.create(employee)

@router.get("/")
async def get_employees():
    return await EmployeeRepo.list_all()

@router.get("/{employee_id}")
async def get_employee(employee_id: str):
    employee = await EmployeeRepo.get_by_id(employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

@router.put("/{employee_id}")
async def update_employee(employee_id: str, req: EmployeeRequest):
    result = await EmployeeRepo.update(employee_id, req.dict())
    if result == 0:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"message": "Employee updated successfully"}

@router.delete("/{employee_id}")
async def delete_employee(employee_id: str):
    result = await EmployeeRepo.delete(employee_id)
    if result == 0:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"message": "Employee deleted successfully"}

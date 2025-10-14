from pydantic import BaseModel

class EmployeeRequest(BaseModel):
    employee_name: str
    employee_company: str

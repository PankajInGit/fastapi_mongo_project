import uuid
from pydantic import BaseModel, Field

class EmployeeModel(BaseModel):
    employee_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    employee_name: str
    employee_company: str  # can be company_id or company_name

from pydantic import BaseModel, Field
import uuid

class EmployeeModel(BaseModel):
    employee_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    employee_name: str
    employee_company: str  

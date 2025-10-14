import uuid
from pydantic import BaseModel, Field

class CompanyModel(BaseModel):
    company_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    company_name: str

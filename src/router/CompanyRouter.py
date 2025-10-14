from fastapi import APIRouter, HTTPException
from src.repo.CompanyRepo import CompanyRepo
from src.models.CompanyModel import CompanyModel
from src.request.CompanyRequest import CompanyRequest

router = APIRouter(prefix="/companies", tags=["Companies"])

@router.post("/")
async def create_company(req: CompanyRequest):
    company = CompanyModel(company_name=req.company_name)
    return await CompanyRepo.create(company)

@router.get("/")
async def get_companies():
    return await CompanyRepo.list_all()

@router.get("/{company_id}")
async def get_company(company_id: str):
    company = await CompanyRepo.get_by_id(company_id)
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    return company

@router.put("/{company_id}")
async def update_company(company_id: str, req: CompanyRequest):
    result = await CompanyRepo.update(company_id, req.dict())
    if result == 0:
        raise HTTPException(status_code=404, detail="Company not found")
    return {"message": "Company updated successfully"}

@router.delete("/{company_id}")
async def delete_company(company_id: str):
    result = await CompanyRepo.delete(company_id)
    if result == 0:
        raise HTTPException(status_code=404, detail="Company not found")
    return {"message": "Company deleted successfully"}

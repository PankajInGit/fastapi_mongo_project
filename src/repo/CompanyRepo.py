from src.database.connection import db
from src.models.CompanyModel import CompanyModel

class CompanyRepo:
    collection = db["companies"]

    @staticmethod
    async def create(company: CompanyModel):
        await CompanyRepo.collection.insert_one(company.dict())
        return {"message": "Company added", "company_id": company.company_id}

    @staticmethod
    async def list_all():
        return await CompanyRepo.collection.find().to_list(100)

    @staticmethod
    async def get_by_id(company_id: str):
        return await CompanyRepo.collection.find_one({"company_id": company_id})

    @staticmethod
    async def update(company_id: str, data: dict):
        result = await CompanyRepo.collection.update_one(
            {"company_id": company_id}, {"$set": data}
        )
        return result.modified_count

    @staticmethod
    async def delete(company_id: str):
        result = await CompanyRepo.collection.delete_one({"company_id": company_id})
        return result.deleted_count

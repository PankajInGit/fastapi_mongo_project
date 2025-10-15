from src.database.connection import db
from src.models.EmployeeModel import EmployeeModel

class EmployeeRepo:
    collection = db["employees"]

    @staticmethod
    async def create(employee: EmployeeModel):
        await EmployeeRepo.collection.insert_one(employee.dict())
        return {"message": "Employee added", "employee_id": employee.employee_id}

    @staticmethod
    async def list_all():
        employees = await EmployeeRepo.collection.find({}, {"_id": 0}).to_list(100)
        return employees

    @staticmethod
    async def get_by_id(employee_id: str):
        return await EmployeeRepo.collection.find_one({"employee_id": employee_id}, {"_id": 0})

    @staticmethod
    async def update(employee_id: str, data: dict):
        result = await EmployeeRepo.collection.update_one(
            {"employee_id": employee_id}, {"$set": data}
        )
        return result.modified_count

    @staticmethod
    async def delete(employee_id: str):
        result = await EmployeeRepo.collection.delete_one({"employee_id": employee_id})
        return result.deleted_count

import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Fetch Mongo credentials
MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
DATABASE_NAME = os.getenv("DATABASE_NAME", "company_db")

# Create Mongo client and select database
client = AsyncIOMotorClient(MONGO_URL)
db = client[DATABASE_NAME]

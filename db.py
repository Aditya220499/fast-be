# db.py
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("MONGO_DB")

client = AsyncIOMotorClient(MONGO_URI)
database = client[DB_NAME]
collection = database["items"]

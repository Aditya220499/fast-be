from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("MONGO_DB", "todo_db")  # Added default value

# Verify environment variables
if not MONGO_URI:
    raise ValueError("MONGO_URI environment variable is not set")

client = AsyncIOMotorClient(MONGO_URI)
database = client[DB_NAME]
collection = database["todos"] 

from bson import ObjectId
from db import collection
from datetime import datetime
from typing import Optional

def serialize_item(item) -> dict:
    return {
        "id": str(item["_id"]),
        "title": item["title"],
        "content": item["content"],
        "category": item["category"],
        "priority": item["priority"],
        "status": item["status"],
        "reminder_at": item.get("reminder_at"),
        "created_at": item.get("created_at"),
        "updated_at": item.get("updated_at"),
        "tags": item.get("tags", []),
        "attachments": item.get("attachments", []),
        "is_favorite": item.get("is_favorite", False)
    }

async def create_item(data: dict):
    # Add timestamps
    data["created_at"] = datetime.utcnow()
    data["updated_at"] = datetime.utcnow()
    
    result = await collection.insert_one(data)
    new_item = await collection.find_one({"_id": result.inserted_id})
    return serialize_item(new_item)

async def get_item(item_id: str):
    item = await collection.find_one({"_id": ObjectId(item_id)})
    if item:
        return serialize_item(item)

async def update_item(item_id: str, data: dict):
    # Add updated timestamp
    data["updated_at"] = datetime.utcnow()
    
    await collection.update_one(
        {"_id": ObjectId(item_id)}, 
        {"$set": data}
    )
    item = await collection.find_one({"_id": ObjectId(item_id)})
    if item:
        return serialize_item(item)

async def delete_item(item_id: str):
    result = await collection.delete_one({"_id": ObjectId(item_id)})
    return result.deleted_count > 0
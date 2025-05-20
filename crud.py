# crud.py
from bson import ObjectId
from db import collection

def serialize_item(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "description": item.get("description"),
        "price": item["price"]
    }

async def create_item(data: dict):
    result = await collection.insert_one(data)
    new_item = await collection.find_one({"_id": result.inserted_id})
    return serialize_item(new_item)

async def get_item(item_id: str):
    item = await collection.find_one({"_id": ObjectId(item_id)})
    if item:
        return serialize_item(item)

async def update_item(item_id: str, data: dict):
    await collection.update_one({"_id": ObjectId(item_id)}, {"$set": data})
    item = await collection.find_one({"_id": ObjectId(item_id)})
    if item:
        return serialize_item(item)

async def delete_item(item_id: str):
    result = await collection.delete_one({"_id": ObjectId(item_id)})
    return result.deleted_count > 0

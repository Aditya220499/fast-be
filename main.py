# main.py
from fastapi import FastAPI, HTTPException
from models import Item, ItemUpdate
from crud import create_item, get_item, update_item, delete_item
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can specify your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/items")
async def create(item: Item):
    return await create_item(item.dict())

@app.get("/items/{item_id}")
async def read(item_id: str):
    item = await get_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.put("/items/{item_id}")
async def update(item_id: str, item: ItemUpdate):
    updated = await update_item(item_id, item.dict(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated

@app.delete("/items/{item_id}")
async def delete(item_id: str):
    success = await delete_item(item_id)
    if not success:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"status": "deleted"}

from fastapi import FastAPI, HTTPException
from models import TodoItem
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

@app.post("/todos")
async def create_todo(todo: TodoItem):
    return await create_item(todo.dict(exclude={'id', 'created_at', 'updated_at'}))

@app.get("/todos/{todo_id}")
async def get_todo(todo_id: str):
    todo = await get_item(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@app.put("/todos/{todo_id}")
async def update_todo(todo_id: str, todo: TodoItem):
    # Exclude id and timestamp fields when updating
    update_data = todo.dict(exclude={'id', 'created_at', 'updated_at'})
    updated = await update_item(todo_id, update_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Todo not found")
    return updated

@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: str):
    success = await delete_item(todo_id)
    if not success:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"status": "deleted"}
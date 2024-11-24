from fastapi import FastAPI, HTTPException
from .database import database, metadata, engine
from .models import todos
from .schemas import Todo, TodoCreate

app = FastAPI()

metadata.create_all(engine)

@app.on_event("startup")
async def startup():
    await database.connect()
    
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.post("/todos/", response_model=Todo)
async def create_todo(todo: TodoCreate):
    query = todos.insert().values(
        title=todo.title,
        description=todo.description,
        completed=todo.completed
    )
    last_record_id = await database.execute(query)
    return {**todo.dict(), "id": last_record_id}

@app.get("/todos/", response_model=list[Todo])
async def read_todos():
    query = todos.select()
    return await database.fetch_all(query)

@app.get("/todos/{todo_id}", response_model=Todo)
async def read_todo(todo_id: int):
    query = todos.select().where(todos.c.id == todo_id)
    record = await database.fetch_one(query)
    if record is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return record

@app.put("/todos/{todo_id}", response_model=Todo)
async def update_todo(todo_id: int, todo: TodoCreate):
    query = todos.update().where(todos.c.id == todo_id).values(
        title=todo.title,
        description=todo.description,
        completed=todo.completed
    )
    await database.execute(query)
    return {**todo.dict(), "id": todo_id}

@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    query = todos.delete().where(todos.c.id == todo_id)
    await database.execute(query)
    return {"message": "Todo deleted successfully"}
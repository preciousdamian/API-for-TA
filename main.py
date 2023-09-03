from fastapi import FastAPI, Response
from models import Todo

app = FastAPI()

@app.get("/")
async def main():
    return {"Message": "Hello API"}

todos_db = []

# All Todos
@app.get("/todos")
async def get_todos():
    return {"Todos": todos_db}

# Get a single todo
@app.get("/todos/{todo_id}")
async def get_todo(todo_id: int):
    for todo in todos_db:
        if todo_id == todo_id:
            return {"todo": todo}
    return {"Msg": "None found"}

# Create a todo
@app.post("/todos")
async def create_todos(todo: Todo):
    todos_db.append(todo)
    return todos_db

# Update a todo
@app.put("/todos/{todo_id}")
async def update_todo(todo_id: int, todo_obj: Todo):
    for todo in todos_db:
        if todo_id == todo_id:
            todo_id = todo_id
            todo_item = todo_obj
            return {"todo": todo}
    return {"Msg": "None found to update"}

# Delete a todo
@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    try:
        for todo in todos_db:
             if todo_id == todo_id:
                todos_db.remove(todo)
                return {{todo_id}: "Has been deleted"}
    except Exception as e:
        return {"Msg": "None found"}  
from enum import Enum
from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/")
async def post():
    return {"message": "hello from the post route"}

@app.put("/")
async def post():
    return {"message": "hello from the put route"}

@app.get("/users")
async def read_users():
    return {"message": "list users route"}

@app.get("/users/{user_id}")
async def get_user(user_id: str):
    return {"message": user_id}

@app.get("/users/me")
async def get_current_user(user: int):
    return {"message": f"this is the current {user}"}

class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetables = "vegetables"
    dairy = "dairy"

@app.get("/foods/{food_name}")
async def get_food(food_name: FoodEnum):
    if food_name == FoodEnum.vegetables:
        return {"food_name": food_name, "message": "you are healthy"}
    if food_name.value == "fruits":
        return {
            "food_name": food_name,
            "message": "you are still healthy but like sweet things"
        }
    return {"food_name": food_name, "message": "I like choco tacos!!!"}

fake_items_db = [{"item_name": "first item"}, {"item_name": "second item"}, {"item_name": "third item"}]
@app.get("/items")
async def list_items(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]

@app.get("/items/{item_id}")
async def get_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"Item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque pellentesque."})
    return item

@app.get("/users/{user_id}/items/{items_id}")
async def get_uset_item(user_id: int, short: bool, item_id: str, q: str | None = None):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque pellentesque."})
        return item


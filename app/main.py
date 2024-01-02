# app/main.py
from fastapi import FastAPI, HTTPException
from app.models.user import UserCreate, User
from app.database.mysql import Database


app = FastAPI()
db = Database()




@app.post("/users/", response_model=User)
def create_user(user: UserCreate):
    user_id = db.create_user(user)
    return db.get_user(user_id)

@app.get("/users/{user_id}", response_model=User)
def read_user(user_id: int):
    user = db.get_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user



@app.put("/users/{user_id}", response_model=bool)
def update_user(user_id: int, user: UserCreate):
    updated = db.update_user(user_id, user)
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return db.get_user(user_id)

@app.delete("/users/{user_id}", response_model=bool)
def delete_user(user_id: int):
    deleted = db.delete_user(user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return deleted


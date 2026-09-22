

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel # FOR CREATE MODEL FOR DATABASE 



app = FastAPI()  # call fastAPI() for routing


# Request/Response model

class User(BaseModel):
    name: str
    email: str
    age: int

# Temporary empty list
users = []


# CREATE
@app.post("/insert_user")
def create_user(user: User):
    new_user = {
    "id": len(users) + 1,
    "name": user.name,
    "email": user.email,
    "age": user.age
    }
    users.append(new_user)
    return {
        "message": "User created successfully",
        "user": new_user
    } 

# READ - Get all users
@app.get("/get_users")
def get_users():
    return users


# READ - Get one user
@app.get("/users/{user_id}")
def get_user(user_id: int):

    for user in users:
        if user["id"] == user_id:
            return user

raise HTTPException(
status_code=404,
detail="User not found"
)


# UPDATE
@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):

    for existing_user in users:
        if existing_user["id"] == user_id:

            existing_user["name"] = user.name
            existing_user["email"] = user.email
            existing_user["age"] = user.age

            return {
            "message": "User updated successfully",
            "user": existing_user
            }
raise HTTPException(
status_code=404,
detail="User not found"
)


# DELETE
@app.delete("/users/{user_id}")
def delete_user(user_id: int):

    for index, user in enumerate(users):
        if user["id"] == user_id:
            deleted_user = users.pop(index)

            return {
            "message": "User deleted successfully",
            "user": deleted_user
            }
            
raise HTTPException(
status_code=404,
detail="User not found"
)
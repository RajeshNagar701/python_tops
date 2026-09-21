
# Run Project : uvicorn main:app --reload
# Open Document : http://127.0.0.1:8000/docs


from fastapi import FastAPI, HTTPException
from sqlmodel import SQLModel, Field, Session, select


app = FastAPI()

@app.get("/")  # decorator 
def welcome():
    return {
        "message": "FastAPI is working"
    }


# --------------------------------
# Model
# --------------------------------

class User(SQLModel, table=True):

    id: int | None = Field(default=None, primary_key=True)
    name: str
    email: str
    mobile: str
    
    
# --------------------------------
# Database
# --------------------------------

from sqlmodel import create_engine

engine = create_engine(
    "sqlite:///users.db",
    echo=True
)

# Create table
SQLModel.metadata.create_all(engine)


#CREATE insert data

@app.post("/users/")   # http://127.0.0.1:8000/users   post data in json by postmen
def create_user(user: User):

    with Session(engine) as session:

        session.add(user)
        session.commit()
        session.refresh(user)

        return user

# READ ALL

@app.get("/users/")   #  http://127.0.0.1:8000/users get data in postman 
def get_users():

    with Session(engine) as session:

        users = session.exec(
            select(User)
        ).all()

        return users

# READ single

@app.get("/users/{user_id}")  # http://127.0.0.1:8000/users/1 
def get_user(user_id: int):

    with Session(engine) as session:

        user = session.get(User, user_id)

        if user is None:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )

        return user
        

# --------------------------------
# UPDATE
# --------------------------------

@app.put("/users/{user_id}")    # http://127.0.0.1:8000/users/1
def update_user(user_id: int, user_data: User):

    with Session(engine) as session:

        user = session.get(User, user_id)

        if user is None:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )

        user.name = user_data.name
        user.email = user_data.email
        user.mobile = user_data.mobile

        session.add(user)
        session.commit()
        session.refresh(user)

        return {
            "message": "User Updated successfully"
        }


# DELETE
# --------------------------------

@app.delete("/users/{user_id}")  # http://127.0.0.1:8000/users/1 
def delete_user(user_id: int):

    with Session(engine) as session:

        user = session.get(User, user_id)

        if user is None:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )

        session.delete(user)
        session.commit()

        return {
            "message": "User deleted successfully"
        }
        
        
"""
With FastAPI + SQLModel, you can easily implement 
LIKE, 
ORDER BY, 
WHERE, 
AND, 
OR, 
greater than, 
less than, 
between, etc.



users = session.exec(select(User)).all()   => GET /users/

like_users = session.exec(select(User).where(User.name.contains(name))).all()   => /users/?name=raj
like_users = session.exec(select(User).where(User.name.startswith(name))).all()   => /users/?name=raj
like_users = session.exec(select(User).where(User.name.endswith(name))).all()   => /users/?name=raj


"""
from fastapi import APIRouter, HTTPException
from app.schemas import UserCreate, UserResponse

router = APIRouter(prefix="/users", tags=["Users"])

# Fake database
users_db = []

@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate):
    user_id = len(users_db) + 1
    new_user = {"id": user_id, **user.dict()}
    users_db.append(new_user)
    return new_user

@router.get("/", response_model=list[UserResponse])
def get_users():
    return users_db

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    for user in users_db:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

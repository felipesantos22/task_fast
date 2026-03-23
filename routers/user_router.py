from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schema.user_schema import UserCreate, UserUpdate, UserResponse, MessageResponse
from services.user_service import UserService
from dependencies import get_db

router = APIRouter(prefix="/users", tags=["users"])
service = UserService()

@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return service.create_user(db, user)


@router.get("/", response_model=list[UserResponse])
def list_users(db: Session = Depends(get_db)):
    return service.repository.find_all(db)


@router.get("/{user_id}", response_model=UserResponse)
def list_users_id(user_id: int, db: Session = Depends(get_db)):
    user = service.repository.find_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    return service.update_user(db, user_id, user)


@router.delete("/{user_id}", response_model=MessageResponse)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    deleted = service.delete_user(db, user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": f"User {user_id} deleted"}

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from core.security import hash_password
from dependencies import take_session
from models import User
from schemas import UserCreate, UserResponse

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.post("/signup", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def signup(payload: UserCreate, db: Session = Depends(take_session)):
    
   email = payload.email.lower().strip()

   new_user = User(
    name=payload.name,
    email=email,
    hashed_password=hash_password(payload.password)
    )
   try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
   except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )
   return new_user
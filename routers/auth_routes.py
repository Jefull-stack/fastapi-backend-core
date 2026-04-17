from fastapi import APIRouter, Depends, HTTPException, status
from models import User
from passlib.context import CryptContext
from sqlalchemy.exc import IntegrityError
from dependencies import take_session
from sqlalchemy.orm import Session
from schemas import UserCreate, UserResponse

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
auth_router = APIRouter(prefix="/auth", tags=["auth"])

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

@auth_router.post("/signup", response_model=UserResponse)
def signup(payload: UserCreate, db: Session = Depends(take_session)):
    
   email = payload.email.lower().strip()
   if len(payload.password) < 8:
        raise HTTPException(
          status_code=status.HTTP_400_BAD_REQUEST,
          detail="Password must be at least 8 characters long"
          )
   new_user = User(
    name=payload.name,
    email=email,
    password=hash_password(payload.password)
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
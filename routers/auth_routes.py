from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from sqlalchemy import inspect

from core.security import verify_and_update, hash_password, create_access_token
from dependencies import take_session
from models import User
from schemas import UserCreate, UserResponse, UserLogin

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.post("/signup", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def signup(payload: UserCreate, db: Session = Depends(take_session)):
    
   email = payload.email.lower().strip()

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

@auth_router.post("/login")
def login(payload: UserLogin, db: Session = Depends(take_session)):
    
    user = db.query(User).filter(User.email == payload.email.lower().strip()).first()

    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    valid, new_hash = verify_and_update(payload.password, user.hashed_password)

    if not valid:
     raise HTTPException(status_code=401, detail="Invalid credentials")
    
    if new_hash:
       user.hashed_password = new_hash
       db.add(user)
       db.commit()
    token = create_access_token({"sub": user.id})
    return {"access_token": token, "token_type": "bearer"}
    
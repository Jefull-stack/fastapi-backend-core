from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from core.security import decode_token
from dependencies.session import take_session
from models import User

bearer = HTTPBearer()

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(bearer),
    db: Session = Depends(take_session)
    ) -> User:
    token = credentials.credentials
    payload = decode_token(token)
    
    if not payload or payload.get("type") != "access":
        raise HTTPException(
            status_code=401,
            detail="Invalid authentication credentials"
            )
            
    user = db.query(User).filter(User.id == payload["sub"]).first()
    
    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
            )
    
    return user
    
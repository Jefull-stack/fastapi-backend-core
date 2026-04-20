from passlib.context import CryptContext
from passlib.exc import UnknownHashError
from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError

from core.config import settings

pwd_context = CryptContext(
    schemes=["argon2", "bcrypt"],
    deprecated="auto"
)
def token_needs_sub(data: dict):
    if "sub" not in data:
        raise ValueError("Token needs 'sub'")
    
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_and_update(plain: str, hashed: str) -> tuple[bool, str | None]:
    try:
        return pwd_context.verify_and_update(plain, hashed)
    except UnknownHashError:
        return False, None

def create_access_token(data: dict, expires_minutes: int | None = None) -> str:
    token_needs_sub(data)
    
    now = datetime.now(timezone.utc)
    minutes = expires_minutes or settings.ACCESS_TOKEN_EXPIRE_MINUTES
    expire = now + timedelta(minutes=minutes)

    payload = {
    "sub": str(data["sub"]),
    "iat": now,
    "exp": expire,
    "type": "access",
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

def create_refresh_token(data: dict) -> str:
    token_needs_sub(data)
    
    now = datetime.now(timezone.utc)
    expire = now + timedelta(days=7)
    
    payload = {
    "sub": str(data["sub"]),
    "iat": now,
    "exp": expire,
    "type": "refresh",
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

def decode_token(token: str) -> dict | None:
    try:
        return jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    except JWTError:
        return None
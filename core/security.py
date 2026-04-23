from passlib.context import CryptContext
from passlib.exc import UnknownHashError
from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError, ExpiredSignatureError

from core.config import settings

pwd_context = CryptContext(
    schemes=["argon2", "bcrypt"],
    deprecated="auto"
)
def token_needs_sub(data: dict):
    sub = data.get("sub")
    if not sub:
        raise ValueError("Token needs a valid 'sub'")
    
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_and_update(plain: str, hashed: str) -> tuple[bool, str | None]:
    try:
        return pwd_context.verify_and_update(plain, hashed)
    except UnknownHashError:
        return False, None

def create_access_token(
    data: dict,
    expires_minutes: int | None = None) -> str:
    token_needs_sub(data)
    
    now = datetime.now(timezone.utc)
    minutes = expires_minutes or settings.ACCESS_TOKEN_EXPIRE_MINUTES
    expire = now + timedelta(minutes=minutes)

    payload = {
        "sub": str(data["sub"]),
        "iat": now,
        "exp": expire,
        "type": "access",
        "iss": "your-api",
        "aud": "your-client"
    }
    return jwt.encode(
        payload,
        settings.ACCESS_SECRET_KEY,
        algorithm=settings.ALGORITHM,
        )

def create_refresh_token(data: dict) -> str:
    token_needs_sub(data)
    
    now = datetime.now(timezone.utc)
    expire = now + timedelta(days=7)
    
    payload = {
        "sub": str(data["sub"]),
        "iat": now,
        "exp": expire,
        "type": "refresh",
        "iss": "your-api",
        "aud": "your-client"
    }
    return jwt.encode(
        payload,
        settings.REFRESH_SECRET_KEY,
        algorithm=settings.ALGORITHM
        )
    
def decode_token(
    token: str,
    expected_type: str) -> dict | None:
    try:
        key = (
            settings.ACCESS_SECRET_KEY
            if expected_type == "access"
            else settings.REFRESH_SECRET_KEY
        )

        payload = jwt.decode(
            token,
            key,
            algorithms=[settings.ALGORITHM],
            audience="your-client",
            issuer="your-api"
        )
        if expected_type and payload.get("type") != expected_type:
            return None

        return payload

    except ExpiredSignatureError:
        return None
    except JWTError:
        return None
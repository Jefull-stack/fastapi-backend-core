from passlib.context import CryptContext
from passlib.exc import UnknownHashError

pwd_context = CryptContext(
    schemes=["argon2", "bcrypt"],
    deprecated="auto"
)

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_and_update(plain: str, hashed: str) -> tuple[bool, str | None]:
    try:
        return pwd_context.verify_and_update(plain, hashed)
    except UnknownHashError:
        return False, None
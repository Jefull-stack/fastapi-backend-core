from pydantic import BaseModel, EmailStr, field_validator

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

    @field_validator("password")
    def validate_password(cls, value):
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters long")
        return value

class UserResponse(BaseModel):
    id: int
    email: str
    name: str
    
    model_config = {"from_attributes": True}

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class OrderCreate(BaseModel):
    user_id: int
    quantity: int

class OrderResponse(BaseModel):
    id: int
    user_id: int
    description: str
    total: float 
    status: str

    model_config = {"from_attributes": True}
    
class RefreshTokenRequest(BaseModel):

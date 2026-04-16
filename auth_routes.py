from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")

async def auth():
    """This is the auth route, you can implement your authentication logic here."""
    return {"message": "you've accessed the auth routes"}
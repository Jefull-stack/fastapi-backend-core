from fastapi import APIRouter

order_router = APIRouter(prefix="/orders", tags=["orders"])

@order_router.get("/")

async def get_orders():
    """This is the orders route, you can implement your order handling logic here."""
    return {"message": "you've accessed the orders routes"}
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependencies.auth import get_current_user
from dependencies.session import take_session
from schemas import OrderCreate
from models import User, Order


order_router = APIRouter(prefix="/orders", tags=["orders"])

@order_router.get("/")
def get_orders(
    session: Session = Depends(take_session), 
    current_user: User = Depends(get_current_user)
    ):
    orders = session.query(Order).all()
    return orders

@order_router.post("/")
async def create_order(
    payload: OrderCreate,
    session: Session = Depends(take_session),
    current_user: User = Depends(get_current_user)
    ):
    new_order = Order(
        user_id=payload.user_id,
        item_name=payload.item_name,
        quantity=payload.quantity,
        price=payload.price
    )
    session.add(new_order)
    session.commit()
    session.refresh(new_order)
    return {"message": f"New order created with success. Order ID: {new_order.id}"}
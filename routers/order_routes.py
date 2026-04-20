from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependencies.auth import take_session
from schemas import OrderCreate, OrderResponse
from models import Order


order_router = APIRouter(prefix="/orders", tags=["orders"])

@order_router.get("/")
def get_orders(session: Session = Depends(take_session)):
    orders = session.query(Order).all()
    return orders


@order_router.post("/")
async def create_order(payload: OrderCreate, session: Session = Depends(take_session)):
    new_order = Order(user_id=payload.user_id)
    session.add(new_order)
    session.commit()
    session.refresh(new_order)
    return {"message": f"New order created with success. Order ID: {new_order.id}"}
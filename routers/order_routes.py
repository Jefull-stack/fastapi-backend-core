from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies.auth import get_current_user
from dependencies.session import take_session
from schemas import OrderCreate, OrderUpdate
from models import User, Order, OrderStatus


order_router = APIRouter(prefix="/orders", tags=["orders"], dependencies=[Depends(get_current_user)])

@order_router.get("/")
async def get_orders(
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

@order_router.get("/{order_id}")
async def get_order(
    order_id: int,
    session: Session = Depends(take_session),
    current_user: User = Depends(get_current_user)
    ):
    order = session.query(Order).filter(Order.id == order_id).first()

    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    if int(order.user_id) != int(current_user.id):  # type: ignore
        raise HTTPException(status_code=403, detail="Not your order")

    return order

@order_router.patch("/{order_id}/cancel")
async def cancel_order(
    order_id: int,
    session: Session = Depends(take_session),
    current_user: User = Depends(get_current_user)
    ):
    order = session.query(Order).filter(Order.id == order_id).first()
    
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    
    if int(order.user_id) != int(current_user.id): #type: ignore
        raise HTTPException (status_code=403, detail="Not your order")
    
    order.status = OrderStatus.cancelled #type: ignore
    session.commit()
    return {"message": f"Order {order_id} cancelled"}

@order_router.put("/{order_id}")
def update_order(
    order_id: int,
    payload: OrderUpdate,
    session: Session = Depends(take_session),
    current_user: User = Depends(get_current_user)
    ):
    order = session.query(Order).filter(Order.id == order_id).first()

    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    if order.user_id != current_user.id:  # type: ignore
        raise HTTPException(status_code=403, detail="Not your order")

    if payload.item_name:
        order.item_name = payload.item_name  # type: ignore
    if payload.quantity:
        order.quantity = payload.quantity  # type: ignore
    if payload.price:
        order.price = payload.price  # type: ignore

    session.commit()
    session.refresh(order)
    return order


@order_router.delete("/{order_id}")
def delete_order(
    order_id: int,
    session: Session = Depends(take_session),
    current_user: User = Depends(get_current_user)
    ):
    order = session.query(Order).filter(Order.id == order_id).first()

    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    if order.user_id != current_user.id:  # type: ignore
        raise HTTPException(status_code=403, detail="Not your order")

    session.delete(order)
    session.commit()
    return {"message": f"Order {order_id} deleted"}
from fastapi import FastAPI
from database.database import Base, engine
from models import User, Order, OrderStatus
from routers.auth_routes import auth_router
from routers.order_routes import order_router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(auth_router)
app.include_router(order_router)
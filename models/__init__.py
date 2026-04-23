# The code defines SQLAlchemy models for users, orders, and products with relationships and attributes
# such as order status and product stock.

from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey, Enum as SQLEnum, DateTime, Numeric
from sqlalchemy.orm import relationship
from enum import Enum
from database.database import Base

class User(Base):__tablename__ = "users"
id = Column(
    Integer,
    primary_key=True,
    index=True
    )
    
name = Column(
    String,
    index=True
    )
    
email = Column(
    String,
    nullable=False,
    unique=True,
    index=True
    )
    
hashed_password = Column(
    String, nullable=False
    )
    
is_active = Column(
    Boolean,
    default=True
    )
    
is_admin = Column(
    Boolean,
    default=False
    )

orders = relationship(
    "Order",
    back_populates="user",
    cascade="all, delete-orphan"
    )

class Product(Base):
    __tablename__ = "products"

    id = Column(
        Integer,
        primary_key=True,
        index=True
        )
    
    name = Column(
        String,
        nullable=False
        )
    
    description = Column(
        String,
        nullable=True
        )
    
    price = Column(
        Numeric(10, 2),
        nullable=False
        )
    
    stock = Column(
        Integer,
        nullable=False
        )




class OrderStatus(str, Enum):
    pending = "pending"
    processing = "processing"
    shipped = "shipped"
    delivered = "delivered"
    cancelled = "cancelled"

class Order(Base):__tablename__ = "orders"

id = Column(
    Integer,
    primary_key=True,
    index=True
    )
    
status = Column(SQLEnum(
    OrderStatus,
    native_enum=True),
    default=OrderStatus.pending
    )
    
user_id = Column(
    Integer,
    ForeignKey("users.id"),
    nullable=False
    )
    
item_name = Column(
    String,
    nullable=False
    )
    
quantity = Column(
    Integer,
    nullable=False
    )
    
price = Column(
    Numeric(10, 2),
    nullable=False
    )

user = relationship(
"User",
back_populates="orders"
)
    
class OrderItem(Base):__tablename__ = "order_items"

id = Column(
    Integer,
    primary_key=True
    )

order_id = Column(
    Integer,
    ForeignKey("orders.id")
    )

product_id = Column(
    Integer,ForeignKey("products.id")
    )
quantity = Column(
    Integer,
    nullable=False
    )

price = Column(
    Float,
    nullable=False
    ) 

order = relationship(
    "Order",
    back_populates="items"
    )

product = relationship("Product")
from sqlalchemy.orm import sessionmaker
from database.database import engine

SessionLocal = sessionmaker(bind=engine)

def take_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
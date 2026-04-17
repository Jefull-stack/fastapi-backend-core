from database.database import engine
from sqlalchemy.orm import sessionmaker

SessionLocal = sessionmaker(bind=engine)

def take_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
# FastAPI Backend Core

REST API built with FastAPI, focused on clean architecture, scalability, and maintainability.  
Includes authentication, modular structure, and database migrations.

---

## 🚀 Features

- User authentication (signup + login)
- Password hashing with bcrypt
- Modular project structure (routers, models, schemas, dependencies)
- Database integration with SQLAlchemy
- Alembic migrations for versioned database changes
- Automatic interactive docs (Swagger UI)

---

## 🧱 Project Structure

project/
├── alembic/ # Database migrations
├── models/ # SQLAlchemy models
├── schemas/ # Pydantic schemas
├── routers/ # API routes
├── dependencies/ # DB/session dependencies
├── database/ # DB connection setup
├── main.py # FastAPI entrypoint
├── alembic.ini
└── requirements.txt

---

##Tech Stack

- FastAPI
- SQLAlchemy
- Alembic
- Pydantic
- Passlib (bcrypt)
- Uvicorn
- Python 3.10+

---

##Installation

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Database Setup
Run migrations with Alembic:
```bash
alembic upgrade head
```

Running the API
```bash
uvicorn main:app --reload
```

API will be available at:
http://127.0.0.1:8000
Docs: http://127.0.0.1:8000/docs

Authentication
POST /auth/signup → Register user
POST /auth/login → Authenticate user (to be implemented / or implemented)

Notes
.env is not included (use your own environment variables)
.venv and local database are ignored in version control

📈 Future Improvements
JWT authentication
Role-based access control
Docker support
Testing (Pytest)

License
MIT

# FastAPI Backend Core

Backend API built with a focus on secure authentication, clean architecture, and continuous system evolution.
This project goes beyond a simple CRUD by applying real-world design decisions and iterative improvements throughout development.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.136-009688?style=flat&logo=fastapi&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-D71F00?style=flat)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-4169E1?style=flat&logo=postgresql&logoColor=white)

---

## Overview

- User registration and authentication with **JWT** (access + refresh token)
- User-level access control (authorization)
- Password hashing with **Argon2** (bcrypt fallback with automatic migration)
- Database integration with **SQLAlchemy** + **PostgreSQL**
- Schema validation with **Pydantic v2**
- Modular and scalable structure
- Full order management CRUD with status control
- User-based data filtering (authorization)
- Order status lifecycle management

---
## Architectural Decisions
- Clear separation between models, schemas, and routes
- Use of refresh tokens to improve authentication flow
- Explicit validation of issuer and audience to prevent token misuse
- Modular structure designed for maintainability and scalability
---

## Future Improvements
- Implement token revocation using jti + blacklist
- Add refresh token rotation
- Introduce database transactions to prevent race conditions
- Implement rate limiting for abuse protection
- Add logging and monitoring
---

## Tech Stack

| Layer | Technology |
|---|---|
| Framework | FastAPI |
| Database | PostgreSQL + SQLAlchemy |
| Auth | JWT via python-jose |
| Hashing | passlib + Argon2 (bcrypt fallback) |
| Validation | Pydantic v2 |
| Server | Uvicorn |

---

## Project Structure

```
fastapi-backend-core/
├── main.py
├── requirements.txt
├── .env.example
├── core/
│   ├── config.py
│   └── security.py
├── database/
│   └── database.py
├── dependencies/
│   ├── auth.py
│   └── session.py
├── models/
├── routers/
│   ├── auth_routes.py
│   └── order_routes.py
└── schemas/
```

---

## Getting Started

### Prerequisites

- Python 3.10+
- PostgreSQL running locally or via Docker

### Installation

```bash
# Clone the repository
git clone https://github.com/Jefull-stack/fastapi-backend-core.git
cd fastapi-backend-core

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your database credentials and secret key
```

### Environment Variables

```env
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
ACCESS_SECRET_KEY: str = "CHANGE_ME"
REFRESH_SECRET_KEY: str = "CHANGE_ME"
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
```

### Running

```bash
uvicorn main:app --reload
```

API available at `http://localhost:8000`  
Interactive docs at `http://localhost:8000/docs`

---

## API Endpoints

### Auth

| Method | Endpoint | Description | Auth required |
|---|---|---|---|
| POST | `/auth/signup` | Register new user | No |
| POST | `/auth/login` | Login and receive tokens | No |
| POST | `/auth/refresh` | Refresh access token | No |
| GET | `/auth/me` | Get current user | Yes |

### Orders

| Method | Endpoint | Description | Auth required |
|---|---|---|---|
| GET | `/orders/` | List orders | Yes |
| POST | `/orders/` | Create order | Yes |
| PUT | `/orders/{id}` | Update order | Yes |
| PATCH | `/orders/{id}/cancel` | Cancel order | Yes |
| DELETE | `/orders/{id}` | Delete order | Yes |

---

## Example Requests

**Register:**
```bash
curl -X POST http://localhost:8000/auth/signup \
  -H "Content-Type: application/json" \
  -d '{"name": "John", "email": "john@email.com", "password": "senha123"}'
```

**Login:**
```bash
curl -X POST http://localhost:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email": "john@email.com", "password": "senha123"}'
```

**Authenticated request:**
```bash
curl http://localhost:8000/auth/me \
  -H "Authorization: Bearer <access_token>"
```

**Create order:**
```bash
curl -X POST http://localhost:8000/orders/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <access_token>" \
  -d '{"user_id": 1, "item_name": "Notebook", "quantity": 1, "price": 1500.00}'
```

---

## About the Project

This project was developed with a focus on practical learning and continuous improvement, applying real backend concepts such as secure authentication, clean code organization, and iterative architectural refinement

---

## License

MIT

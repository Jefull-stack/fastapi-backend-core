# FastAPI Backend Core

REST API built with FastAPI, focusing on clean architecture, security, and scalability.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.136-009688?style=flat&logo=fastapi&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-D71F00?style=flat)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-4169E1?style=flat&logo=postgresql&logoColor=white)

---

## Features

- User registration and authentication with **JWT** (access + refresh token)
- Password hashing with **Argon2** (bcrypt fallback with automatic migration)
- Database integration with **SQLAlchemy** + **PostgreSQL**
- Schema validation with **Pydantic v2**
- Clean architecture: routers, models, schemas, and dependencies separated
- Full order management CRUD with status control

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
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
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

## License

MIT

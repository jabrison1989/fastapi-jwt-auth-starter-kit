# FastAPI Auth Service

A modular authentication microservice built with FastAPI and JWT, designed to demonstrate secure authentication patterns, service decomposition, and reusable system design.

## Problem
Applications frequently need authentication, but building it repeatedly leads to inconsistent security practices and duplicated effort.

## Solution
This project provides a reusable authentication service with JWT-based access control, clean separation of concerns, and extensible architecture for integration into larger systems.

## Key Design Decisions
- Stateless JWT authentication for scalability
- Modular service structure for maintainability
- Environment-driven configuration for deployment flexibility
- Default SQLite with support for scaling to MySQL/Postgres

## Why It Matters

This project demonstrates how to:
- Design a reusable service instead of one-off logic
- Separate concerns between routing, services, and data models
- Implement secure authentication workflows
- Build systems that can evolve from prototype to production

These patterns are directly applicable to larger distributed systems and platform engineering work.

## Features

- Secure user registration & login
- JWT-based authentication
- Bcrypt password hashing
- SQLite by default (MySQL/Postgres-ready)
- Modular architecture (easy to extend)
- Simple route prefixing (`/auth/*`)
- Environment-based configuration
- Pydantic schemas + SQLAlchemy models
- Swagger API docs out-of-the-box

---

## 📁 Project Structure

```
auth_service/
├── app/
│   ├── models/          # SQLAlchemy DB models
│   ├── routers/         # FastAPI route handlers
│   ├── schemas/         # Pydantic request/response models
│   ├── services/        # Auth logic, token creation, DB
│   └── main.py          # FastAPI app w/ CORS + route registration
├── .env.example         # Sample config
├── requirements.txt     # Python dependencies
```

---

## Getting Started

### 1. Clone the project

Clone the repository and run locally:

```bash
git clone https://github.com/jabrison1989/fastapi-jwt-auth-starter-kit.git
cd fastapi-jwt-auth-starter-kit
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Copy `.env.example` to `.env` and adjust as needed:

```bash
cp .env.example .env
```

### 4. Run the server

```bash
docker-compose up --build
```

Visit Swagger docs at [http://localhost:8000/docs](http://localhost:8000/docs)

---

## API Routes

| Method | Route           | Description         |
|--------|------------------|---------------------|
| POST   | `/auth/register` | Create a new account |
| POST   | `/auth/login`    | Get access token     |
| GET    | `/auth/me`       | Get current user (JWT required) |

---

## Configuration Options (`.env`)

| Key                  | Description                     |
|----------------------|---------------------------------|
| `SECRET_KEY`         | Secret used to sign JWT tokens |
| `ALGORITHM`          | JWT algorithm (default: HS256) |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Token lifespan in minutes |

---

## Example Request

### Register

```json
POST /auth/register
{
  "email": "user@example.com",
  "password": "supersecurepassword"
}
```

### Login

```json
POST /auth/login
{
  "email": "user@example.com",
  "password": "supersecurepassword"
}
```

Returns:

```json
{
  "access_token": "your.jwt.token",
  "token_type": "bearer"
}
```

> **Swagger Tip**: When authenticating using the Swagger “Authorize” button, paste **only the token value** — do **not** include `Bearer `, Swagger will add it for you automatically.

---

## Limitations / Tradeoffs

This project is intentionally lightweight and does not include advanced production features such as:
- Rate limiting
- Token revocation / rotation strategies
- Multi-factor authentication
- Distributed session management

It is designed as a foundation to demonstrate authentication patterns and can be extended to meet production requirements.

---

## 📄 License

MIT — free for personal and commercial use.  
You may **not** resell this code as a standalone product.

---

## Author
Jacob Brison

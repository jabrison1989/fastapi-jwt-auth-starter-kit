# FastAPI Auth Service

A modular authentication microservice built with FastAPI and JWT, designed to demonstrate secure authentication patterns, service decomposition, and reusable system design.

---

## Problem

Applications frequently require authentication, but rebuilding it repeatedly leads to inconsistent security practices and duplicated effort.

---

## Solution

This project provides a reusable authentication service with JWT-based access control, clean separation of concerns, and an extensible architecture suitable for integration into larger systems.

The service is structured as a layered application separating routing, business logic, and data access, making it easy to extend or integrate into distributed environments.

---

## Key Design Decisions

* Stateless JWT authentication for scalability
* Modular service structure for maintainability
* Environment-driven configuration for deployment flexibility
* Default SQLite with support for scaling to MySQL/Postgres

---

## Why It Matters

This project highlights key engineering patterns used in production systems:

* Design reusable services instead of one-off implementations
* Separate concerns between routing, services, and data models
* Implement secure authentication workflows
* Build systems that evolve from prototype to production
* Design stateless services that scale horizontally

These patterns are directly applicable to distributed systems and platform engineering.

---

## Features

* Secure user registration and login
* JWT-based authentication
* Bcrypt password hashing
* SQLite by default (MySQL/Postgres-ready)
* Modular architecture (easy to extend)
* Route prefixing (`/auth/*`)
* Environment-based configuration
* Pydantic schemas + SQLAlchemy models
* Swagger API documentation out-of-the-box

---

## Project Structure

```
auth_service/
├── app/
│   ├── models/          # SQLAlchemy DB models
│   ├── routers/         # FastAPI route handlers
│   ├── schemas/         # Pydantic request/response models
│   ├── services/        # Auth logic, token creation, DB access
│   └── main.py          # FastAPI application entry point
├── .env.example         # Sample configuration
├── requirements.txt     # Python dependencies
```

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/jabrison1989/fastapi-jwt-auth-starter-kit.git
cd fastapi-jwt-auth-starter-kit
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

```bash
cp .env.example .env
```

Update values in `.env` as needed.

### 4. Run the service

```bash
docker-compose up --build
```

Access Swagger docs at:
http://localhost:8000/docs

---

## API Routes

| Method | Route            | Description           |
| ------ | ---------------- | --------------------- |
| POST   | `/auth/register` | Create a new account  |
| POST   | `/auth/login`    | Obtain access token   |
| GET    | `/auth/me`       | Retrieve current user |

---

## Configuration Options

| Key                           | Description                    |
| ----------------------------- | ------------------------------ |
| `SECRET_KEY`                  | JWT signing key                |
| `ALGORITHM`                   | JWT algorithm (default: HS256) |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Token expiration time          |

---

## Example Requests

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

### Response

```json
{
  "access_token": "your.jwt.token",
  "token_type": "bearer"
}
```

> **Swagger Tip:** When using the "Authorize" button, paste only the token value. Swagger automatically adds the `Bearer` prefix.

---

## Limitations / Tradeoffs

This project is intentionally lightweight and does not include advanced production features such as:

* Rate limiting
* Token revocation or rotation strategies
* Multi-factor authentication
* Distributed session management

It is designed as a foundation to demonstrate authentication patterns and can be extended for production use.

---

## License

MIT — free for personal and commercial use.
Resale of this code as a standalone product is not permitted.

---

## Author

Jacob Brison

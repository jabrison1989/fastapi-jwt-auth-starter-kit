# 🔐 FastAPI AuthService

A lightweight, plug-and-play authentication microservice built with FastAPI and JWT.  
Perfect for indie developers, SaaS prototypes, and internal tools that need secure user management — fast.

---

## ✅ Features

- 🔒 Secure user registration & login
- 🔐 JWT-based authentication
- 🧂 Bcrypt password hashing
- 📦 SQLite by default (MySQL/Postgres-ready)
- 🧱 Modular architecture (easy to extend)
- 🔌 Simple route prefixing (`/auth/*`)
- ⚙️ Environment-based configuration
- 📄 Pydantic schemas + SQLAlchemy models
- 🧪 Swagger API docs out-of-the-box

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

## 🚀 Getting Started

### 1. Unzip the project

After purchasing, extract the `.zip` file to your development directory:

```bash
unzip fastapi-authservice.zip
cd auth_service
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

## 🔑 API Routes

| Method | Route           | Description         |
|--------|------------------|---------------------|
| POST   | `/auth/register` | Create a new account |
| POST   | `/auth/login`    | Get access token     |
| GET    | `/auth/me`       | Get current user (JWT required) |

---

## ⚙️ Configuration Options (`.env`)

| Key                  | Description                     |
|----------------------|---------------------------------|
| `SECRET_KEY`         | Secret used to sign JWT tokens |
| `ALGORITHM`          | JWT algorithm (default: HS256) |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Token lifespan in minutes |

---

## 🧪 Example Request

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

> 💡 **Swagger Tip**: When authenticating using the Swagger “Authorize” button, paste **only the token value** — do **not** include `Bearer `, Swagger will add it for you automatically.

---

## 🧠 Recommended Use Cases

- 🕹 Indie games or MMO backends
- 🚀 SaaS MVPs needing fast auth
- 🛠 Developer tools with gated access
- 👥 Any solo project that doesn't need full-blown Auth0

---

## ⚠️ Disclaimer

This is a lightweight, developer-focused starter service built for speed and simplicity.  
It’s not a full-scale auth system like Auth0 or Firebase.

While I’ve tested everything and structured it cleanly, this is not actively maintained as a long-term project — it's meant to save you time by giving you a solid foundation to build on.

If you're looking for enterprise-grade support or constant updates, this may not be the right fit.  
But if you're a solo dev or small team who needs to plug in authentication fast — this will get you moving.

---

## 📄 License

MIT — free for personal and commercial use.  
You may **not** resell this code as a standalone product.

---

## 👋 Built by Jacob Brison

If this saved you time, consider leaving a ⭐ rating or sharing the link with other developers who might find it useful.

Have questions or feedback? Reach out to me directly — I’d love to hear from you.
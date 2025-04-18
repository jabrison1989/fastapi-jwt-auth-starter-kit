# FastAPI JWT Auth Starter Kit

FastAPI JWT authentication starter kit with login, register, Docker, and bearer token routes.

---

## 📦 Get the Kit
⚠️ This is a paid starter kit. The source code is **not included** in this repository.  
    It’s available for download via Gumroad:
👉 [Download the Starter Kit on Gumroad](https://brijac3.gumroad.com/l/jwt-auth-kit)

[👉 Jump to FAQ](#-faq)

A plug-and-play authentication microservice built with FastAPI, JWT, and Docker support.

---

## 📦 What's in the Kit?

- Register/Login routes
- JWT token auth
- Bcrypt password hashing
- Docker-ready setup
- Swagger docs
- SQLite by default, Postgres-compatible

---

## ⚡ Quick Preview

- `/register`, `/login`, and `/me` routes included
- JWT tokens using `python-jose`
- Dockerized with `.env` support

---

## 🔍 Screenshots

**Register route**  
![register](register_route.png)

**Login route**  
![login](login_route.png)

**Token returned used in Swagger UI Authorization**  
![token](authorization_token.png)

**/me route (get user)**  
![get user](get_user_route.png)



---

## 📦 Get the Kit Again (in case you scrolled fast)

👉 [https://brijac3.gumroad.com/l/jwt-auth-kit](https://brijac3.gumroad.com/l/jwt-auth-kit)

---

## ❓ FAQ

**Q: Can I use this in production?**  
A: Yes — for small apps, prototypes, internal tools, and indie projects.  
It's built with security best practices (hashed passwords, JWT, route protection).  
For enterprise use, you should add rate limiting, logging, 2FA, and additional auth flows.

**Q: Is this better than Auth0 or Firebase?**  
A: This kit is meant to be simple and self-hosted — no external dependencies.  
It’s great if you want full control and don't want to integrate large third-party auth platforms.

**Q: Does it support OAuth or social login?**  
A: Not yet. It’s built as a minimal starting point.  
You can extend it to include OAuth, refresh tokens, or role-based access.

**Q: What database does it use?**  
A: SQLite by default, with easy Docker support for Postgres or MySQL.

**Q: Is this project actively maintained?**  
A: It’s not under full-time development — but it’s clean, documented, and plug-and-play ready.


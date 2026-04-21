# A Job Board API

# ## A platform where companies can post jobs and candidates can apply - built with a scalable, production-grade FastAPI backend

🏛️ Architecture First

```
                    [ Client: Browser / Mobile / Postman ]
                                        |
                                   HTTP Request
                                        |
                              ┌─────────────────┐
                              │   FastAPI App   │  ← Our Backend
                              │  (Uvicorn ASGI) │
                              └────────┬────────┘
                                       │
                ┌──────────────────────┼──────────────────────┐
                │                      │                      │
        ┌───────▼──────┐     ┌─────────▼────────┐   ┌────────▼──────┐
        │  Auth Router  │    │   Jobs Router    │   │  Applications │
        │  /auth/*      │    │   /jobs/*        │   │  Router       │
        └───────┬───────┘    └─────────┬────────┘   └────────┬──────┘
                │                      │                     │
                └──────────────────────┼─────────────────────┘
                                       │
                              ┌─────────▼────────┐
                              │   Database Layer │
                              │  SQLAlchemy ORM  │
                              └─────────┬────────┘
                                        │
                              ┌─────────▼─────────┐
                              │    PostgreSQL DB  │
                              └───────────────────┘
```

📁 Folder Structure

```
jobnest/
│
├── app/                        # Everything lives here
│   ├── __init__.py
│   │
│   ├── main.py                 # FastAPI app entry point
│   │
│   ├── core/                   # App-wide config & security
│   │   ├── __init__.py
│   │   ├── config.py           # Environment variables
│   │   └── security.py         # JWT, password hashing
│   │
│   ├── db/                     # Database connection
│   │   ├── __init__.py
│   │   └── session.py          # SQLAlchemy engine & session
│   │
│   ├── models/                 # Database table definitions
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── job.py
│   │   └── application.py
│   │
│   ├── schemas/                # Request & Response shapes (Pydantic)
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── job.py
│   │   └── application.py
│   │
│   ├── routers/                # API route handlers
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── jobs.py
│   │   └── applications.py
│   │
│   └── services/               # Business logic (brain of the app)
│       ├── __init__.py
│       ├── auth_service.py
│       ├── job_service.py
│       └── application_service.py
│
├── tests/                      # All tests live here
│   └── test_auth.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

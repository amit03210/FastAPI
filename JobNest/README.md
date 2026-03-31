# A Job Board API

# ## A platform where companies can post jobs and candidates can apply - built with a scalable, production-grade FastAPI backend

```
                    [ Client: Browser / Mobile / Postman ]
                                        |
                                   HTTP Request
                                        |
                              ┌─────────────────┐
                              │   FastAPI App    │  ← Our Backend
                              │  (Uvicorn ASGI)  │
                              └────────┬────────┘
                                       │
                ┌──────────────────────┼──────────────────────┐
                │                      │                       │
        ┌───────▼──────┐     ┌─────────▼────────┐   ┌────────▼───────┐
        │  Auth Router  │     │   Jobs Router     │   │  Applications  │
        │  /auth/*      │     │   /jobs/*         │   │  Router        │
        └───────┬───────┘     └─────────┬─────────┘   └────────┬───────┘
                │                       │                        │
                └───────────────────────┼────────────────────────┘
                                        │
                              ┌─────────▼────────┐
                              │   Database Layer  │
                              │  SQLAlchemy ORM   │
                              └─────────┬─────────┘
                                        │
                              ┌─────────▼─────────┐
                              │    PostgreSQL DB  │
                              └───────────────────┘
```

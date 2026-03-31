### 🧠 Why This Structure?

| Folder      | Real-World Reason                                             |
| ----------- | ------------------------------------------------------------- |
| `routers/`  | Separates concerns - each feature has its own file            |
| `models/`   | Maps to DB tables - change here, DB changes                   |
| `schemas/`  | Controls what data comes IN and goes OUT of API               |
| `services/` | Business logic separate from routes - testable, reusable      |
| `core/`     | Config & security in one place - easy to change               |
| `.env`      | Secrets never hardcoded - this is non-negotiable in real apps |



### 🧠 Why This Structure?

| Folder      | Real-World Reason                                             |
| ----------- | ------------------------------------------------------------- |
| `routers/`  | Separates concerns - each feature has its own file            |
| `models/`   | Maps to DB tables - change here, DB changes                   |
| `schemas/`  | Controls what data comes IN and goes OUT of API               |
| `services/` | Business logic separate from routes - testable, reusable      |
| `core/`     | Config & security in one place - easy to change               |
| `.env`      | Secrets never hardcoded - this is non-negotiable in real apps |

Phase 1 — Foundation (Steps 1-3)  
├── Step 1: Project Setup
├── Step 2: Configuration & .env
└── Step 3: Database Connection

Phase 2 — Core Models (Steps 4-6)
├── Step 4: User Model + Registration
├── Step 5: Login + JWT Auth
└── Step 6: Role-based Access (Recruiter / Candidate)

Phase 3 — Features (Steps 7-10)
├── Step 7: Company Profiles
├── Step 8: Job Listings (CRUD)
├── Step 9: Job Search & Filters
└── Step 10: Applications + Resume Upload

Phase 4 — Production (Steps 11-13)
├── Step 11: Error Handling & Logging
├── Step 12: Testing with Pytest
└── Step 13: Deployment (Render/Railway)

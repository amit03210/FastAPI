from fastapi import FastAPI
from app.core.config import settings


app = FastAPI(
    title=settings.APP_NAME,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION,
    debug=settings.DEBUG,
)


@app.get("/health")
def health_check():
    """
    Health check endpoint.
    Real-world use: Load balancer ping this to know if the server is alive.
    """
    return {
        "status": "ok",
        "app": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "allowed host": settings.ALLOWED_HOSTS,
        "email": settings.CONTACT_EMAIL,
        "version": settings.APP_VERSION,
    }


@app.on_event("startup")
async def startup():
    print("🚀 JobNest API is starting up...")


@app.on_event("shutdown")
async def shutdown():
    print("🛑 JobNest API is shutting down...")

from fastapi import FastAPI

app = FastAPI(title="JobNest", description="A scalable job board backend built with FastAPI", version="1.0.0")

@app.get("/")
def health_check():
    """
    Health check endpoint.
    Real-world use: Load balancer ping this to know if the server is alive.
    """
    return {"status":"load",  "app" : "JobNest"}
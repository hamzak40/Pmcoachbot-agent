from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def healthz_root():
    # This endpoint is mounted at /api/healthz
    # Hitting /api/healthz will trigger this "/"
    return {"ok": True, "service": "pm-coachbot", "status": "healthy", "via": "/api/healthz"}

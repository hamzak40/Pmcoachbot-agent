from fastapi import FastAPI

# This function is mounted at /api/index
app = FastAPI(title="PM CoachBot")

@app.get("/")
async def root():
    return {
        "ok": True,
        "message": "PM CoachBot API is running.",
        "try": ["/api/healthz", "/api/index/healthz"]
    }

@app.get("/healthz")
async def healthz():
    return {"ok": True, "service": "pm-coachbot", "via": "/api/index/healthz", "status": "healthy"}

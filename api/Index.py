from fastapi import FastAPI

app = FastAPI(title="PM CoachBot")

@app.get("/")
async def root():
    return {"ok": True, "message": "PM CoachBot API is running.", "try": ["/api/healthz", "/api/index/healthz"]}

@app.get("/healthz")
async def healthz():
    return {"ok": True, "service": "pm-coachbot", "status": "healthy", "via": "/api/index/healthz"}

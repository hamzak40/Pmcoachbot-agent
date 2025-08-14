from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def healthz_root():
    return {"ok": True, "service": "pm-coachbot", "via": "/api/healthz", "status": "healthy"}

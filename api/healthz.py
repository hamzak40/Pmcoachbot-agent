from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def healthz():
    return {"ok": True, "service": "pm-coachbot", "status": "healthy"}

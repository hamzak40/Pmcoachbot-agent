from fastapi import FastAPI

# This function is mounted at /api/healthz
# So define the route at "/" (not "/healthz")
app = FastAPI()

@app.get("/")
async def healthz_root():
    return {"ok": True, "service": "pm-coachbot", "status": "healthy", "via": "/api/healthz"}

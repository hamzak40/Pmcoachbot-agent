from fastapi import FastAPI

# Vercel mounts this file at /api/index
app = FastAPI(title="PM CoachBot")

@app.get("/")
async def root():
    return {"ok": True, "message": "PM CoachBot API is running.", "try": ["/api/healthz", "/api/index/healthz"]}

# Also respond on ANY subpath so we can verify routing easily
@app.get("/{path:path}")
async def index_any(path: str):
    if path.rstrip("/") == "healthz":
        return {"ok": True, "service": "pm-coachbot", "via": "/api/index/healthz", "status": "healthy"}
    return {"ok": True, "path": f"/api/index/{path}"}

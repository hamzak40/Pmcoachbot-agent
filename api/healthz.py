from fastapi import FastAPI

# Vercel mounts this file at /api/healthz
app = FastAPI()

# Return healthy JSON for both the base path and ANY subpath
@app.get("/")
async def healthz_root():
    return {"ok": True, "service": "pm-coachbot", "via": "/api/healthz", "status": "healthy"}

@app.get("/{path:path}")
async def healthz_any(path: str):
    return {"ok": True, "service": "pm-coachbot", "via": "/api/healthz", "status": "healthy", "path": path}

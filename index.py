from fastapi import FastAPI
app = FastAPI()

@app.get("/healthz")
async def healthz():
    return {"ok": True, "service": "pm-coachbot", "status": "healthy"}


app = FastAPI(title='PM CoachBot (Modern Vercel Config)')

@app.get('/')
async def root():
    return {'ok': True, 'message': 'PM CoachBot API is running. Try /healthz'}

@app.get('/healthz')
async def healthz():
    return {'ok': True, 'service': 'pm-coachbot', 'status': 'healthy'}

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from api.routers import health, runs, jira, slack, gumroad, access

app = FastAPI(title='PM CoachBot Subscription Agent (MVP)')

@app.get('/')
async def root():
    return {'ok': True, 'message': 'PM CoachBot Agent running. Try /healthz or POST /runs/plan'}

app.include_router(health.router)
app.include_router(access.router, prefix='/access', tags=['access'])
app.include_router(gumroad.router, prefix='/gumroad', tags=['gumroad'])
app.include_router(runs.router, prefix='/runs', tags=['runs'])
app.include_router(jira.router, prefix='/jira', tags=['jira'])
app.include_router(slack.router, prefix='/slack', tags=['slack'])

@app.exception_handler(Exception)
async def generic_handler(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={'error':'SERVER_ERROR','message':str(exc)})

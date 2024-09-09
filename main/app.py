from fastapi import FastAPI, HTTPException, status
from fastapi import Request

from main.config import SERVER_STATS_TOKEN
from main.models import ServerStats
from main.stats import get_stats

app = FastAPI()


@app.get("/test/")
async def server_test(request: Request):
    if request.headers.get("token") != SERVER_STATS_TOKEN:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return {"status": "working"}


@app.get("/server_stats/", response_model=ServerStats)
async def get_server_stats(request: Request):
    if request.headers.get("token") != SERVER_STATS_TOKEN:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return get_stats()

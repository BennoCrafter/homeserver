from typing import List
from fastapi import Request, APIRouter
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import Optional
from fastapi import Query


observice_router = APIRouter()

# Templates directory
templates = Jinja2Templates(directory="app/routes/observice/templates")

class Log(BaseModel):
    timestamp: float
    name: str
    level: str
    message: str
    file: str
    line: int

logs_db: List[Log] = []

@observice_router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "logs": logs_db})

@observice_router.post("/api/logs/")
async def add_log(log: Log):
    logs_db.insert(0, log)
    return {"log_name": log.name, "message": "Log added successfully"}

@observice_router.delete("/api/logs/")
async def clear_logs():
    logs_db.clear()
    return {"message": "All logs have been cleared successfully"}


@observice_router.get("/api/logs/")
def get_logs(level: Optional[str] = None, limit: int = Query(100, ge=1)):
    filtered_logs = logs_db
    if level:
        filtered_logs = [log for log in logs_db if log.level== level]

    if limit > len(filtered_logs):
        limit = len(filtered_logs)
    filtered_logs = filtered_logs[:limit]
    return filtered_logs

@observice_router.get("/logs", response_class=HTMLResponse)
def view_logger(request: Request):
    return templates.TemplateResponse("logger.html", {"request": request, "logs": logs_db})

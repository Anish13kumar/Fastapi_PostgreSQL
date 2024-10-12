from fastapi import FastAPI, Request, Depends
from app.router import root
import uvicorn
from app.database import get_master_db, get_slave_db, Base, MASTER_ENGINE, SLAVE_ENGINE
from app import models
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session

app = FastAPI()

# Bind both Master and Slave engines
Base.metadata.create_all(bind=MASTER_ENGINE)
Base.metadata.create_all(bind=SLAVE_ENGINE)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(name="index.html", request=request)


app.include_router(root.router)

if __name__ == "__main__":
    uvicorn.run("run:app", host="127.0.0.1", port=8000, reload=True)

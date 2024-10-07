from fastapi import FastAPI,Request
from app.router import root
import uvicorn
from app.database import engine
from app import models
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse



app = FastAPI()
models.Base.metadata.create_all(bind=engine)
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_root(request:Request):
    return templates.TemplateResponse(name="index.html",request=request)


app.include_router(root.router)
templates = Jinja2Templates(directory="templates")

if __name__ == "__main__":
    uvicorn.run("run:app",host="127.0.0.1",port=8000,reload=True)
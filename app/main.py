from fastapi import FastAPI, BackgroundTasks, HTTPException, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

from fastapi.templating import Jinja2Templates

app = FastAPI()

#* confirugacion carpeta plantillas   pip install --upgrade pydantic fastapi   pip install --upgrade pydantic fastapi   pip install --upgrade pydantic fastapi   pip install --upgrade pydantic fastapi   pip install --upgrade pydantic fastapi
templates = Jinja2Templates(directory="templates")


#* configuracion de cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/index", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})





from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path


app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")

templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    # Render a simple home page with links
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/inventory", response_class=HTMLResponse)
def inventory(request: Request):
    return templates.TemplateResponse("inventory.html", {"request": request})

@app.get("/wishlist", response_class=HTMLResponse)
def wishlist(request: Request):
    return templates.TemplateResponse("wishlist.html", {"request": request})

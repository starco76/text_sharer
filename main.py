from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uuid

app = FastAPI()

# پوشه قالب‌ها
templates = Jinja2Templates(directory="templates")

# دیتاست ساده برای نگه داشتن متن‌ها
texts = {}


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/create_link", response_class=HTMLResponse)
def create_link(request: Request, user_text: str = Form(...)):
    # ساخت یه شناسه یکتا
    text_id = str(uuid.uuid4())
    texts[text_id] = user_text
    return templates.TemplateResponse("index.html", {
        "request": request,
        "link": f"/text/{text_id}"
    })


@app.get("/text/{text_id}", response_class=HTMLResponse)
def show_text(request: Request, text_id: str):
    text = texts.get(text_id, "متن یافت نشد.")
    return templates.TemplateResponse("show_text.html", {
        "request": request,
        "text": text
    })

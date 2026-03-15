import json
import uuid
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path

app = FastAPI()
templates = Jinja2Templates(directory="templates")


DB_FILE = Path("db.json")

# بارگذاری دیتابیس از فایل


def load_db():
    if DB_FILE.exists():
        with open(DB_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

# ذخیره دیتابیس به فایل


def save_db(data):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/create_link", response_class=HTMLResponse)
def create_link(request: Request, user_text: str = Form(...)):
    db = load_db()
    text_id = str(uuid.uuid4())
    db[text_id] = user_text
    save_db(db)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "link": f"/text/{text_id}"
    })


@app.get("/text/{text_id}", response_class=HTMLResponse)
def show_text(request: Request, text_id: str):
    db = load_db()
    text = db.get(text_id, "متن یافت نشد.")
    return templates.TemplateResponse("show_text.html", {
        "request": request,
        "text": text
    })

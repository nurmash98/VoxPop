from fastapi import FastAPI, Request, Response, Form
from fastapi.templating import Jinja2Templates

from fastapi.responses import RedirectResponse
app = FastAPI()
templates = Jinja2Templates(directory="templates")

comments = []

@app.get("/")
def index(request: Request, page: int = 1, limit: int = 3):
    new_comments = comments[(page - 1)*limit:page*limit]
    return templates.TemplateResponse("index.html", {"request": request, "comments": new_comments, "pages" : (len(comments) + limit - 1)//limit , "limit" : limit, "page": page})
@app.get("/comment")
def form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/comment")
def add_comment(request: Request, text: str = Form(), type: str = Form()):
    comments.append({"text": text, "type": type})
    return RedirectResponse("/", status_code=303)






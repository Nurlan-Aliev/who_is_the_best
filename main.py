from fastapi import FastAPI, Request, Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from db_connecnt import database, grow_count
from fastapi.responses import RedirectResponse


app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def read_item(
    request: Request,
):
    """
    Get first page
    """
    response = templates.TemplateResponse(
        request=request,
        name="index.html",
    )
    response.delete_cookie("first_time")
    return response


@app.get("/arina_the_best")
async def arina_the_best(request: Request):
    """
    page client you choose Arina
    """
    count = database.get("arina") if database.get("arina") else 0
    return templates.TemplateResponse(
        request=request,
        name="arina_the_best.html",
        context={"count": count},
    )


@app.get("/nur_the_best")
async def nur_the_best(request: Request):
    """
    page client you choose Nurlan
    """
    count = database.get("nurlan") if database.get("nurlan") else 0

    return templates.TemplateResponse(
        request=request,
        name="nur_the_best.html",
        context={"count": count},
    )


@app.post("/arina_the_best")
async def choose_arina_the_best(cookie: Request, response: Response):
    """
    post for choose Arina
    """
    cookie = cookie.cookies.get("first_time")
    response = RedirectResponse("/arina_the_best", status_code=302)

    if not cookie:
        response.set_cookie("first_time", "i am here")
        grow_count("arina")
    return response


@app.post("/nur_the_best")
async def choose_nur_the_best(cookie: Request):
    """
    post for choose Nurlan
    """
    cookie = cookie.cookies.get("first_time")
    response = RedirectResponse("/nur_the_best", status_code=302)

    if not cookie:
        response.set_cookie("first_time", "i am here")
        grow_count("nurlan")
    return response

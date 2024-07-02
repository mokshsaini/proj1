from fastapi import APIRouter, Form
from models import records
from config.db import database
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.responses import HTMLResponse
from typing import Annotated, Any
from datetime import date

router1 = APIRouter()

templates = Jinja2Templates(directory = 'templates')

@router1.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html"
    )
@router1.post("/submit", response_class=HTMLResponse)
async def submit(request: Request, select: Annotated[int, Form()] ):
    # print(edit)
    if select:
        return templates.TemplateResponse(
           request=request, name="fetch.html"
      )
    else:
        return templates.TemplateResponse(
            request=request, name="add.html"
      )


@router1.post('/submit/add', response_model=records)
async def add(
    Name: str = Form(...),
    Date: str = Form(...),
    BP: str = Form(...),
    Weight_in_kg: str = Form(...),
    Gender: str = Form(...),
    Height_in_meters: str = Form(...),
    Fever: str = Form("False")

     ):
    form = {'Name': Name,
    'Date': Date,
    'BP': BP,
    'Weight_in_kg': Weight_in_kg,
    'Gender': Gender,
    'Height_in_meters': Height_in_meters,
    'Fever': Fever}
    # form2 = await request.form()
    # formd2= dict(form2)
    # print(formd2)
    # print(form, 'yo')
    # form = await request.form()

    record = database.proj1.health_data.insert_one(form)
    # print(dict(form))
    return {'success':True}

@router1.post('/submit/fetch')
async def add(request:Request):
    form = await request.form()
    form_dict = dict(form)

    key_list = []
    for key in form_dict.keys():
        if form_dict[key] == '':
            key_list.append(key)
    for key in key_list:
        form_dict.pop(key)
    
    print(form_dict)
    # query = {"$or": [{"Name": form_dict.get("Name")}, {"date": form_dict.get("date")}, {"Weight_in_kg": form_dict.get("Weight_in_kg")}, {"Height_in_meters": form_dict.get("Height_in_meters")}, {"BP": form_dict.get("BP")}]}

    record = database.proj1.health_data.find(form_dict)
    recordlist = list(record)
    print(recordlist)
    print(list(record))
    return templates.TemplateResponse(
            "fetch_result.html", {"request":request, 'recordlist':recordlist}
            )
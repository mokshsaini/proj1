from fastapi import APIRouter, Form, HTTPException
from models import Records, Records_fetch
from config.db import database
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.responses import HTMLResponse
from datetime import date
from typing import Annotated

router1 = APIRouter()

templates = Jinja2Templates(directory = 'templates')

@router1.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html"
    )

@router1.post("/submit", response_class=HTMLResponse)
async def submit(request: Request, select: Annotated[int, Form()] ):
    if select:
        return templates.TemplateResponse(
           request=request, name="fetch.html"
      )
    else:
        return templates.TemplateResponse(
            request=request, name="add.html"
      )

@router1.post('/submit/add')
async def add(request:Request):
    form = await request.form()
    form_dict = dict(form)
    record = Records(**form_dict)
    record.date_conversion()
    try:
        result = database.proj1.health_data.insert_one((record.model_dump()))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
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
    
    try:
        record = Records_fetch(**form_dict)
        record.date_conversion()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    validated_data = record.model_dump()
    key_list = []
    for key in validated_data.keys():
        if validated_data[key] == None:
            key_list.append(key)
    for key in key_list:
        validated_data.pop(key)

    record = database.proj1.health_data.find(validated_data)
    recordlist = list(record)
    return templates.TemplateResponse(
            "fetch_result.html", {"request":request, 'recordlist':recordlist}
            )

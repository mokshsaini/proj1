from fastapi import FastAPI, Request
from routes import router1

from fastapi.staticfiles import StaticFiles

from pydantic import BaseModel




app = FastAPI()
app.include_router(router1)





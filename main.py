from fastapi import FastAPI
from routes import router1

from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.include_router(router1)





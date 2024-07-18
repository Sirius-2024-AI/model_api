from fastapi import FastAPI
from starlette import status
from starlette.responses import Response

from scr.utils import *

app = FastAPI()

@app.get("/ping")
def pong():
    return {"ping": "pong!"}
from typing import Union
from fastapi import FastAPI
import requests
import json
from datetime import date
from app.core.config import get_app_settings


def get_application() -> FastAPI:
    args = get_app_settings()
    application = FastAPI(**args)

    return application


app = get_application()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/abc/{code}/{date}")
def read_averge(code: str, date: date):
    url = f'http://api.nbp.pl/api/exchangerates/rates/A/{code}/{date}/?format=json'
    req = requests.get(url)
    response = req.json()
    avg = response['rates'][0]['mid']
    return avg





if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)

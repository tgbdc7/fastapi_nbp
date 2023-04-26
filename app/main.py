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


@app.get("/average/{code}/{date}")
def read_average(code: str, date: date):
    url = f'http://api.nbp.pl/api/exchangerates/rates/A/{code}/{date}/?format=json'
    req = requests.get(url)
    response = req.json()
    avg = response['rates'][0]['mid']
    return avg


@app.get("/minmax/{code}/{topCount}")
def read_minmax(code: str, topCount: int):
    url = f"http://api.nbp.pl/api/exchangerates/rates/a/{code}/last/{topCount}/?format=json"
    req = requests.get(url)
    response = req.json()
    minmax_list = [x['mid'] for x in response['rates']]
    minmax = {'min': min(minmax_list), 'max': max(minmax_list)}
    return minmax


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)

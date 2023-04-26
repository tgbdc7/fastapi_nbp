import requests
from datetime import datetime
from fastapi import APIRouter

router = APIRouter(prefix="/exchangerates")


@router.get("/{code}/{data}")
def read_exchanges(code: str, date: datetime.date):
    req = requests.get(f'http://api.nbp.pl/api/exchangerates/rates/A/{code}/{date}/?format=json')
    return req

import requests
from fastapi import APIRouter
from collections import Counter
from datetime import date

router = APIRouter(prefix="/exchangerates")


@router.get("/average/{code}/{date}")
def read_average(code: str, date: date):
    url = f'http://api.nbp.pl/api/exchangerates/rates/A/{code}/{date}/?format=json'
    req = requests.get(url)
    response = req.json()
    avg = response['rates'][0]['mid']
    res = {"average": avg}
    return res


@router.get("/minmax/{code}/{topCount}")
def read_minmax(code: str, topCount: int):
    url = f"http://api.nbp.pl/api/exchangerates/rates/a/{code}/last/{topCount}/?format=json"
    req = requests.get(url)
    response = req.json()
    minmax_list = [x['mid'] for x in response['rates']]
    res = {'min': min(minmax_list), 'max': max(minmax_list)}
    return res


@router.get("/difference/{code}/{topCount}")
def read_difference(code: str, topCount: int):
    url = f"http://api.nbp.pl/api/exchangerates/rates/c/{code}/last/{topCount}/?format=json"

    req = requests.get(url)
    response = req.json()
    difference: list = [round(x['ask'] - x['bid'], 4) for x in response['rates']]
    max_diff = max(difference)
    most_common_diff = Counter(difference).most_common(1)[0][0]
    res = {"max difference": max_diff, "most common difference": most_common_diff}
    return res

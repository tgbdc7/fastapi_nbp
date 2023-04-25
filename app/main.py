from typing import Union
from fastapi import FastAPI

from app.core.config import get_app_settings


def get_application() -> FastAPI:
    args = get_app_settings()
    application = FastAPI(**args)

    return application


app = get_application()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get('/exchanges/{code}/{date}')
def read_exchanges(code: str, date: str):
    return code


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8888)

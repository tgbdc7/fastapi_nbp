from fastapi import FastAPI
from app.core.config import get_app_settings
from app.api import exchangerates


def get_application() -> FastAPI:
    args = get_app_settings()
    application = FastAPI(**args)

    return application


app = get_application()
app.include_router(exchangerates.router)


@app.get("/")
def get_root():
    return {"message": "Great, it works. Now you can check our endpoints."}

import logging
from typing import Callable, Coroutine

from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

from tp2.webserver import root


# logging middleware
async def log_request(request: Request, call_next):
    if "log" in request.query_params and request.query_params["log"] == "ignore":
        return await call_next(request)
    method = request.method
    url_path = request.url.path
    ip = request.client.host
    port = request.client.port
    logging.info(f"handling {url_path!r} | {method=} | address={ip}:{port}")
    return await call_next(request)


def create_app(startup: Callable[[None], Coroutine[None, None, None]]):
    app = FastAPI()
    app.add_middleware(BaseHTTPMiddleware, dispatch=log_request)
    app.include_router(root.router)

    app.on_event("startup")(startup)

    return app

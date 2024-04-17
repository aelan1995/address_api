from typing import Union
from dependencies import get_query_token, get_token_header
from internal import admin
from routers import address, users, token
from fastapi import FastAPI

app = FastAPI()

app.include_router(token.router)
app.include_router(address.router)



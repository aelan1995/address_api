<<<<<<< HEAD
from typing import Union
from dependencies import get_query_token, get_token_header
from internal import admin
from routers import address, users, token
from fastapi import FastAPI

app = FastAPI()

app.include_router(token.router)
app.include_router(address.router)


=======
from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()

security = HTTPBasic()


@app.get("/users/me")
def read_current_user(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    return {"username": credentials.username, "password": credentials.password}
>>>>>>> 60797d5d7c8ac47e350a2214a2de3b8e3bcf7105

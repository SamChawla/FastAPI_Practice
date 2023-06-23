from enum import Enum
from typing import Optional

from fastapi import FastAPI, Response, status

from router import blog_get

app = FastAPI()
app.include_router(blog_get.router)


class Status(str, Enum):
    active = "Active"
    inactive = "InActive"


@app.get(
    "/",
    tags=["home"],
    summary="Home Page",
    description="This is a home page",
    response_description="Returns Home Page",
)
def index():
    """Base Endpoint

    Returns:
        json: message
    """
    return {"message": "Hello World"}


@app.post("/", tags=["home"])
def index2():
    """Base Endpoint with post

    Returns:
        json: message
    """
    return {"message": "Hello World"}


# PreDefined Values
@app.get("/user/status/{status}", tags=["user"])
def user_type(status: Status):
    return "Status is : {status}"

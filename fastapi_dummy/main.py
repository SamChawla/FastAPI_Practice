from enum import Enum
from typing import Optional

from fastapi import FastAPI, Query

app = FastAPI()


class Status(str, Enum):
    active = "Active"
    inactive = "InActive"


@app.get("/")
def index():
    """Base Endpoint

    Returns:
        json: message
    """
    return {"message": "Hello World"}


@app.post("/")
def index2():
    """Base Endpoint with post

    Returns:
        json: message
    """
    return {"message": "Hello World"}


@app.get("/blogs/")
def blogs():
    """Returns Blog content

    Returns:
        list: json list of blogs
    """
    return [{"blog_id": 1, "content": "This is a sample Blog"}]


# Path Params
@app.get("/blogs/{id}")
def blog(id: int):
    """Returns Blog content

    Returns:
        json: blog content
    """
    return {"blog_id": id, "content": "This is a sample Blog"}


# PreDefined Values
@app.get("/user/status/{status}")
def user_type(status: Status):
    return "Status is : {status}"


# Query Params with Default values
@app.get("/blogs/")
def get_blogs(page=1, page_size=10):
    data = []
    for val in range(1, int(page_size) + 1):
        data.append({"blog_id": val, "content": "This is a sample text"})
    return data


# Query Params with Optional values
@app.get("/blogs/optional/")
def get_blogs_optional(page=1, page_size=Query(default=10)):
    data = []
    for val in range(1, int(page_size) + 1):
        data.append({"blog_id": val, "content": "This is a sample text"})
    return data

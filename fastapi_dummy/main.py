from enum import Enum
from typing import Optional

from fastapi import FastAPI, Query, Response, status

app = FastAPI()


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


@app.get(
    "/blogs/",
    tags=["blog", "list"],
    summary="Fetch all blogs",
    description="Replicated the functionality of fetching blogs",
)
def blogs():
    """Returns Blog content

    Returns:
        list: json list of blogs
    """
    return [{"blog_id": 1, "content": "This is a sample Blog"}]


# Path Params
@app.get("/blogs/{id}", status_code=status.HTTP_200_OK, tags=["blog"])
def blog(id: int, response: Response):
    """Returns Blog content

    - **id** mandatory path parameter

    Returns:
        json: blog data
    """
    if id > 10:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": "Content not available"}
    else:
        response.status_code = status.HTTP_200_OK
        return {"blog_id": id, "content": "This is a sample Blog"}


# PreDefined Values
@app.get("/user/status/{status}", tags=["user"])
def user_type(status: Status):
    return "Status is : {status}"


# Query Params with Default values
@app.get("paginated/blogs/", tags=["paginated"])
def get_blogs(page=1, page_size=10):
    data = []
    for val in range(1, int(page_size) + 1):
        data.append({"blog_id": val, "content": "This is a sample text"})
    return data


# Query Params with Optional values
@app.get("/blogs/optional/", tags=["blog"])
def get_blogs_optional(page=1, page_size=Query(default=10)):
    data = []
    for val in range(1, int(page_size) + 1):
        data.append({"blog_id": val, "content": "This is a sample text"})
    return data

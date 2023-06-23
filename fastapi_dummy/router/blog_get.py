from enum import Enum
from typing import Optional

from fastapi import APIRouter, Query, Response, status


router = APIRouter(prefix="/blogs", tags=["blog"])


@router.get(
    "/",
    tags=["list"],
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
@router.get("/{id}", status_code=status.HTTP_200_OK)
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


# Query Params with Default values
@router.get("/paginated", tags=["paginated"])
def get_blogs(page=1, page_size=10):
    data = []
    for val in range(1, int(page_size) + 1):
        data.routerend({"blog_id": val, "content": "This is a sample text"})
    return data


# Query Params with Optional values
@router.get("/optional")
def get_blogs_optional(page=1, page_size=Query(default=10)):
    data = []
    for val in range(1, int(page_size) + 1):
        data.append({"blog_id": val, "content": "This is a sample text"})
    return data

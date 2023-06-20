from fastapi import FastAPI

app = FastAPI()


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

@app.get("/blogs/{id}")
def blog(id: int):
    """Returns Blog content

    Returns:
        json: blog content
    """
    return {"blog_id": id, "content": "This is a sample Blog"}

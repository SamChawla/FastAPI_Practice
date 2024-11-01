""" This is the main file of the FastAPI project. """

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    """ This is the root path of the FastAPI project. """
    return {"message": "Hello World"}

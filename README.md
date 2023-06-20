# FastAPI

- `FastAPI` is created by Sebastian Ramirez
- It provides a better option for building REST APIs and microservices.

## Packages Required

```bash
pip install fastapi
pip install uvicorn[standard]
pip install python-multipart
```

Other option that you can try to utilize the full capabilities of FastAPI, better option is:

```bash
pip install fastapi[all]
pip install uvicorn
pip install bcrypt
```

- The `python-multipart` module is required to create a REST API that handles form parameters.
- The installed `uvicorn`, is an ASGI-based server that will run your FastAPI applications. 
- The uvicorn server has the capability to run both synchronous and asynchronous services.

## Running Application

- To locally run our application, we need to execute the following command: `uvicorn main:app --reload`
from bcrypt import checkpw
from fastapi import FastAPI
from fastapi.responses import FileResponse

#You can replace app with your preferred but valid Python variable name, such as main_app, forum, or myapp.
app = FastAPI()

favicon_path = 'favicon.ico'

@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse(favicon_path)

@app.get("/index")
def index():
    return {"message": "Welcome to the world of FastAPI"} 

valid_users = {
    "test":"fjllenfjlnejwnfe"
}

@app.get("/login/")
def login(username: str, password: str):
    if valid_users.get(username) == None:
        return {"message": "user does not exist"}
    else:
        user = valid_users.get(username)
        if checkpw(password.encode(), user.passphrase.encode()):
            return user
        else:
            return {"message": "invalid user"}
        

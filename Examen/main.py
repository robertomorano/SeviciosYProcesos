from fastapi import FastAPI
from routers import  auth_users, colegio, alumno


app = FastAPI()


app.include_router(alumno.router)
app.include_router(colegio.router)
app.include_router(auth_users.router)


@app.get("/")
def greeting():
    return "hello world"
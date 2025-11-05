from fastapi import FastAPI
from routers import users, product, auth_user
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.include_router(users.router)
app.include_router(product.router)
app.include_router(auth_user.router)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def greeting():
    return "hello world"
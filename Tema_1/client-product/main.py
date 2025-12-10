from fastapi import FastAPI
from routers import  product, auth_user, product_db
from fastapi.staticfiles import StaticFiles

app = FastAPI()


app.include_router(product_db.router)
#app.include_router(product.router)
app.include_router(auth_user.router)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def greeting():
    return "hello world"

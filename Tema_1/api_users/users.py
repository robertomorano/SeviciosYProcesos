from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id : int
    name : str
    surname : str
    age : int

lista_user = [User(id = 1, name= "Paco", surname= "Peres", age= 15),
              User(id = 2, name= "Pacdasdas", surname= "Peres", age= 15), 
              User(id = 3, name= "Paadsadaco", surname= "Peres", age= 15)]

@app.get("/users")
def users():
    return lista_user

@app.get("/users/{id_user}")
def get_user(id_user: int):
    users = [user for user in lista_user if user.id == id_user]
    return users[0] if (len(users) !=0) else {"a tu casa": "TONTO"}

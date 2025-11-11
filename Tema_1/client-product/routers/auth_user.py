from pydantic import BaseModel
from fastapi import APIRouter, Depends, HTTPException
import jwt
from jwt.exceptions import InvalidTokenError
from pwdlib import PasswordHash
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm, OAuth2PasswordRequestFormStrict

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

#algoritmo de encriptacion
ALGORITHM = "HS256"
#Duracion Token
ACCES_TOKEN_EXPIRE_MINUTES = 3

#seed para el token
SECRET_KEY= "e35fc165ea266a56c864d9a73b6b1ba2f0de16c908e528a739ae36a9b88d8656"

#Objeto calculo hash
password_hash = PasswordHash.recommended()


router = APIRouter()


class User(BaseModel):
        username: str
        fullname: str
        email: str
        disabled: bool
class UserDB(User):
        password: str
    
users_db = {
        "userario" : {
                "username" : "userario",
                "fullname" : "user sario",
                "email" : "mera.dime@loqsea.com",
                "disabled": True,
                "password" : "55463" 
        },
        "PIENA POLLO" : {
                "username" : "PIENA POLLO",
                "fullname" : "user sario",
                "email" : "mera.dime2@loqsea.com",
                "disabled": False,
                "password": "12354"
        }
        
}

@router.post("/register", status_code=201)
def register(user:UserDB):
        if user.username not in users_db:
            hashed_password = password_hash.hash(user.password)
            user.password = hashed_password
            users_db[user.username] = user
            return user
        else:
               raise HTTPException(status_code= 409, detail="User already exists")
        
@router.post("/login")
async def login(form: OAuth2PasswordRequestFormStrict = Depends()):
       if form.username in users_db:
              if form.password_ha
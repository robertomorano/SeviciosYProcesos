from datetime import datetime, timezone, timedelta
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
        },
        "userariho"   : {
                "username": "userariho",
                "fullname": "user sario",
                "email": "meradsa.dime@loqsea.com",
                "disabled": True,
                "password": "$argon2id$v=19$m=65536,t=3,p=4$pMGQCZp/VrMC35OBKG7mzg$457CpdKbso4rZ7oYhW/h6nMV4SFiQtNJpKmEL2/SDWE"#55454663
}
        
}

@router.get("/login")
def getUsers():
        return users_db

@router.post("/register", status_code=201)
def register(user:UserDB):
        if user.username not in users_db:
            hashed_password = password_hash.hash(user.password)
            user.password = hashed_password
            users_db[user.username] = user.model_dump()
            return user
        else:
               raise HTTPException(status_code= 409, detail="User already exists")
        
@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
       
        user_form = users_db.get(form.username)
        if user_form:
                user = UserDB(**user_form)
        try:
                if user.username in users_db:
                        if password_hash.verify(form.password, user.password):
                                expire = datetime.now(timezone.utc)+timedelta(minutes=ACCES_TOKEN_EXPIRE_MINUTES)
                                access_token = {"sub": user.username, "exp": expire}
                                token = jwt.encode(access_token, SECRET_KEY, algorithm=ALGORITHM)
                                return {"access_toke": token, "token_type":"bearer"}
        except:
                raise HTTPException(status_code=400, detail="autencacion")
        raise HTTPException(status_code=401, detail="Usuersuario o contraseña incorremcotos")

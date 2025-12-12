from bson import ObjectId
from fastapi import APIRouter, Depends, HTTPException
from db.models.alumno import Alumno
from db.schemas.alumno import alumno_schema, alumnos_schema
from db.client import db_client

from .auth_users import authentication

router = APIRouter(prefix="/alumnos", tags = ["alumnos"])


cursos_list = ["1ESO", "2ESO", "3ESO", "4ESO", "1BACH", "2BACH"]



def find_alumno(id : str):
    try:
        alumno = alumno_schema(db_client.local.alumno.find_one({"_id":ObjectId(id)}))
        return Alumno(**alumno)
    except:
        return {"Alumno": "No encontrado"}


#GET Method

@router.get("/")
def alumnos():
    return alumnos_schema(db_client.local.alumno.find())

@router.get("/{id}")
def get_alumno(id: str):
    return find_alumno(id)

@router.get("/")
def alumnos(curso : str):
    try:
        alumnos = alumnos_schema(db_client.local.alumno.find({"curso": curso}))
        return alumnos
    except:
        return {"Alumno": "No encontrado"}
@router.get("/")
def alumnos(distrito : str):
    try:
        alumnos = alumnos_schema(db_client.local.alumno.find({"distrito": distrito}))
        return alumnos
    except:
        return {"Alumno": "No encontrado"}


#POST Method

@router.post("/", status_code=201, response_model=Alumno)
def add_alumno(alumno: Alumno):#,authorized=Depends(authentication)
    try:
        if not (db_client.local.colegio.find_one({"_id": ObjectId(alumno.id_colegio) })):
            raise HTTPException(status_code=409, detail="Colegio not exists")
    except:
        raise HTTPException(status_code=409, detail="Colegio not exists")
    if (alumno.curso not in cursos_list):
        raise HTTPException(status_code=409, detail="Curso no valido")

    alumno_dict = alumno.model_dump()

    del alumno_dict["id"]

    id = db_client.local.alumno.insert_one(alumno_dict).inserted_id
    
    alumno_dict["id"] = str(id)

    return Alumno(**alumno_dict)
    

#PUT Method

@router.put("/{id}", status_code=200, response_model=Alumno)
def modify_alumno(id:str, alumno:Alumno):    #, authorized=Depends(authentication)
    
    alumno_update = alumno.model_dump(exclude_unset=True, exclude={"id"})

    updated_doc = db_client.local.alumno.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": alumno_update},
        return_document=True 
    )

    raise HTTPException(status_code=404, detail="alumno not found")

#region DELETE Method

@router.delete("/{id}")
def delete_alumno(id:str):#,  authorized=Depends(authentication)
    try:
        success = db_client.local.alumno.find_one_and_delete({"id":(id)})
        if not success:
            raise HTTPException(status_code=404, detail="alumno not found")     
        return success
    except:
        raise HTTPException(status_code=200, detail="eliminado")

from bson import ObjectId
from fastapi import APIRouter, Depends, HTTPException
from db.schemas.alumno import alumnos_schema
from db.models.colegio import Colegio
from db.schemas.colegio import colegio_schema, colegios_schema
from db.client import db_client

from .auth_users import authentication

router = APIRouter(prefix="/colegios", tags = ["colegios"])


tipos_list = ["publico", "concertado", "privado"]



def find_colegio(id : str):
    try:
        colegio = colegio_schema(db_client.local.colegio.find_one({"_id":ObjectId(id)}))
        return Colegio(**colegio)
    except:
        return {"Colegio": "No encontrado"}


#GET Method

@router.get("/")
def colegios():
    return colegios_schema(db_client.local.colegio.find())

@router.get("/{id}")
def get_colegio(id: str):
    return find_colegio(id)

@router.get("/{id_colegio}/alumnos")
def get_alumnos_colegio(id_colegio):
    colegio = find_colegio(id_colegio)
    if not (colegio):
        raise HTTPException(status_code=404, detail="colegio not found")
    alumnos = alumnos_schema(db_client.local.alumno.find({"id_colegio": str(id_colegio)}))
    return alumnos

@router.get("/estadisticas/distritos")
def get_stats():
    colegios = colegios_schema(db_client.local.colegio.find())
    diccionario = {}
    try:
        for colegio in colegios:
            
            alumnos = get_alumnos_colegio(colegio.id)
            diccionario[colegio.distrito] += 1
            diccionario[alumnos] += len(alumnos) 
    except:
        raise HTTPException(status_code=404, detail="colegio not found")



#POST Method

@router.post("/", status_code=201, response_model=Colegio)
def add_colegio(colegio: Colegio):#,authorized=Depends(authentication)
    
    
    if (colegio.tipo not in tipos_list):
        raise HTTPException(status_code=409, detail="tipo no valido")

    colegio_dict = colegio.model_dump()

    del colegio_dict["id"]

    id = db_client.local.colegio.insert_one(colegio_dict).inserted_id
    
    colegio_dict["id"] = str(id)

    return Colegio(**colegio_dict)
    


#region DELETE Method

@router.delete("/{id}")
def delete_colegio(id:str ):# authorized=Depends(authentication)
    counter = 0
    colegio = db_client.local.colegio.find_one_and_delete({"_id": ObjectId(id)})
    if not colegio:
        raise HTTPException(status_code=404, detail="colegio not found")     
    if (db_client.local.alumno.find({"id_colegio": str(colegio.id)})):
        alumnos = db_client.local.alumno.find_one_and_delete({"id_colegio": str(colegio.id)})
        counter+=1
    
    return {
        "colegio_borrado": colegio.name,
        "alumnos_borrados": counter
    }
            

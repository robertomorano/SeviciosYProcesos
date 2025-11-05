from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/director", tags = ["products"])

class Director(BaseModel):
    id : int
    dni : str
    name : str
    surname : str
    email : str

director_list = [Director(id = 1, dni= "202043Y", name= "Paco", surname= "Peres", email= "a@b.c"),
              Director(id = 2, dni= "202043Y",name= "Pacdasdas", surname= "Peres", email= "a@b.c"), 
              Director(id = 3, dni= "202043Y",name= "Paadsadaco", surname= "Peres", email= "a@b.c")]

def next_id():
    return (max(director_list, key=id).id+1)


def find_product(id : int):
    product = [product for product in director_list if product.id == id]
    return product[0] if (len(product) !=0) else {"Esta": "Mal"}

#GET Method

@router.get("/")
def products():
    return director_list

@router.get("/{id_product}")
def get_product(id_product: int):
    product = [product for product in director_list if product.id == id_product]
    return product[0] if (len(product) !=0) else {"Esta": "Mal"}


#products/?id=
@router.get("")
def products(id : int):
    return find_product(id)


#POST Method

@router.post("/", status_code=201, response_model=Director)
def add_product(product: Director):
    product.id = next_id()
    director_list.append(product)
    return product

#PUT Method

@router.put("/{id}", status_code=200, response_model=Director)
def modify_product(id:int, product:Director):    
    for index, saved_product in enumerate(director_list):
        if saved_product.id == id:
            product.id=id
            director_list[index] = product
            return product

    raise HTTPException(status_code=404, detail="director not found")

#DELETE Method

@router.delete("/{id}")
def delete_product(id:int):
    
    for saved_product in director_list:
    
        if saved_product.id == id:
            director_list.remove(saved_product)
            return {}
    raise HTTPException(status_code=404, detail="director not found") 
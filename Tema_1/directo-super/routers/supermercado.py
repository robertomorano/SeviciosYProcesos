from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/supermarket", tags = ["products"])

class Supermercado(BaseModel):
    id : int
    fecha : str
    direction : str
    surface : float
    id_director : int

supermarket_list = [Supermercado(id = 1, fecha= "2020-01-01", direction= "Calle Falsa 123", surface= 150.5, id_director=1),
                    Supermercado(id = 2, fecha= "2021-02-02", direction= "Avenida Siempre Viva 742", surface= 200.0, id_director=2), 
              Supermercado(id = 3, fecha= "2022-03-03", direction= "Plaza Mayor 1", surface= 300.75, id_director=3)]

def next_id():
    return (max(supermarket_list, key=id).id+1)


def find_product(id : int):
    product = [product for product in supermarket_list if product.id == id]
    return product[0] if (len(product) !=0) else {"Esta": "Mal"}

#GET Method

@router.get("/")
def products():
    return supermarket_list

@router.get("/{id_product}")
def get_product(id_product: int):
    product = [product for product in supermarket_list if product.id == id_product]
    return product[0] if (len(product) !=0) else {"Esta": "Mal"}

@router.get("/query")
def products(id : int):
    return find_product(id)


#POST Method

@router.post("/", status_code=201, response_model=Supermercado)
def add_product(product: Supermercado):
    product.id = next_id()
    supermarket_list.append(product)
    return product

#PUT Method

@router.put("/{id}", status_code=200, response_model=Supermercado)
def modify_product(id:int, product:Supermercado):    
    for index, saved_product in enumerate(supermarket_list):
        if saved_product.id == id:
            product.id=id
            supermarket_list[index] = product
            return product

    raise HTTPException(status_code=404, detail="supermarket not found")

#DELETE Method

@router.delete("/{id}")
def delete_product(id:int):
    
    for saved_product in supermarket_list:
    
        if saved_product.id == id:
            supermarket_list.remove(saved_product)
            return {}
    raise HTTPException(status_code=404, detail="supermarket not found") 
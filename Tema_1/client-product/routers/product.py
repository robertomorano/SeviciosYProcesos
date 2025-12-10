"""from fastapi import APIRouter, Depends, HTTPException
from db.models.product import Product
from db.shemas.product import product_schema, products_schemas

from .auth_user import authentication

router = APIRouter(prefix="/products", tags = ["products"])



product_list = [Product(id = 1, name= "Paco", description= "Peres", price= 15, id_cliente=1),
              Product(id = 2,name= "Pacdasdas", description= "Peres", price= 15, id_cliente=2), 
              Product(id = 3,name= "Paadsadaco", description= "Peres", price= 15, id_cliente=3)]

def next_id():
    return (max(product_list, key=id).id+1)


def find_product(id : int):
    product = [product for product in product_list if product.id == id]
    return product[0] if (len(product) !=0) else {"Esta": "Mal"}

#GET Method

@router.get("/")
def products():
    return product_list

@router.get("/{id_product}")
def get_product(id_product: int):
    product = [product for product in product_list if product.id == id_product]
    return product[0] if (len(product) !=0) else {"Esta": "Mal"}

@router.get("/query")
def products(id : int):
    return find_product(id)


#POST Method

@router.post("/", status_code=201, response_model=Product)
def add_product(product: Product, authorized=Depends(authentication)):
    product.id = next_id()
    product_list.append(product)
    return product

#PUT Method

@router.put("/{id}", status_code=200, response_model=Product)
def modify_product(id:int, product:Product):    
    for index, saved_product in enumerate(product_list):
        if saved_product.id == id:
            product.id=id
            product_list[index] = product
            return product

    raise HTTPException(status_code=404, detail="product not found")

#DELETE Method

@router.delete("/{id}")
def delete_product(id:int):
    
    for saved_product in product_list:
    
        if saved_product.id == id:
            product_list.remove(saved_product)
            return {}
    raise HTTPException(status_code=404, detail="product not found") 
    """
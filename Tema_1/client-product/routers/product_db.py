from bson import ObjectId
from fastapi import APIRouter, Depends, HTTPException
from db.models.product import Product
from db.shemas.product import product_schema, products_schema
from db.client import db_client

from .auth_user import authentication

router = APIRouter(prefix="/products", tags = ["products"])


def next_id():
    return (max(product_list, key=id).id+1)


def find_product(id : int):
    product = [product for product in db_client.local.product.find() if product.id == id]
    return product[0] if (len(product) !=0) else {"Esta": "Mal"}

#GET Method

@router.get("/")
def products():
    return products_schema(db_client.local.product.find())

@router.get("/{id_product}")
def get_product(id_product: int):
    product = [product for product in db_client.local.product.find() if product.id == id_product]
    return product[0] if (len(product) !=0) else {"Esta": "Mal"}

@router.get("/query")
def products(id : int):
    return find_product(id)


#POST Method

@router.post("/", status_code=201, response_model=Product)
def add_product(product: Product, authorized=Depends(authentication)):
    
    if type(find_product()):
        pass
    

#PUT Method

@router.put("/{id}", status_code=200, response_model=Product)
def modify_product(id:int, product:Product):    
    
    product_update = product.model_dump(exclude_unset=True, exclude={"id"})

    updated_doc = db_client.local.product.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": product_update},
        return_document=True # Return the modified document
    )

    raise HTTPException(status_code=404, detail="product not found")

#DELETE Method

@router.delete("/{id}")
def delete_product(id:int):
    success = db_client.local.product.find_one_and_delete({"_id": ObjectId(id)})
    if not success:
        raise HTTPException(status_code=404, detail="product not found")     
    return success
            
    
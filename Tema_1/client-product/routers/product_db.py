from bson import ObjectId
from fastapi import APIRouter, Depends, HTTPException
from db.models.product import Product
from db.shemas.product import product_schema, products_schema
from db.client import db_client

from .auth_user import authentication

router = APIRouter(prefix="/productsdb", tags = ["products"])






def find_product(id : str):
    try:
        product = product_schema(db_client.test.product.find_one({"_id":ObjectId(id)}))
        return Product(**product)
    except:
        return {"Esta": "Mal"}

def search_product(name:str, id_cliente:int):
    try:
        product = product_schema(db_client.test.products.find_one({"name":name, "id_cliente":id_cliente}))
        return Product(**product)
    except:
        print("anasd")
        return {"error ": "User not found"}

#GET Method

@router.get("/")
def products():
    return products_schema(db_client.test.product.find())

@router.get("/{id_product}")
def get_product(id_product: str):
    return find_product(id_product)

@router.get("/query")
def products(id : int):
    return find_product(id)


#POST Method

@router.post("/", status_code=201, response_model=Product)
def add_product(product: Product):#authorized=Depends(authentication)
    
    if type(search_product(product.name, product.id_cliente)) == Product:
        raise HTTPException(status_code=409, detail="Product already exists")
    
    product_dict = product.model_dump()

    del product_dict["id"]

    id = db_client.test.product.insert_one(product_dict).inserted_id
    
    product_dict["id"] = str(id)

    return Product(**product_dict)
    

#PUT Method

@router.put("/{id}", status_code=200, response_model=Product)
def modify_product(id:str, product:Product):    
    
    product_update = product.model_dump(exclude_unset=True, exclude={"id"})

    updated_doc = db_client.test.product.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": product_update},
        return_document=True 
    )

    raise HTTPException(status_code=404, detail="product not found")

#region DELETE Method

@router.delete("/{id}")
def delete_product(id:str):
    success = db_client.test.product.find_one_and_delete({"_id": ObjectId(id)})
    if not success:
        raise HTTPException(status_code=404, detail="product not found")     
    return success
            

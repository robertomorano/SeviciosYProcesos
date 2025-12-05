

def product_schema(product) -> dict:
    return {
        "id" : str(product["_id"]),
       "name": product["name"],
       "description" : product["description"],
       "price" : product["price"],
       "id_cliente": product["id_cliente"]

    }

def products_schema(users) -> list:
    return [product_schema(user) for user in users]
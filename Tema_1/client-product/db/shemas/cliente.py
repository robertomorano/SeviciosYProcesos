def cliente_schema(cliente) -> dict:
    return {
        "id" : str(cliente["_id"]),
        "dni": cliente["dni"],
       "name": cliente["name"],
       "surname" : cliente["surname"],
       "phone" : cliente["phone"],
       "email": cliente["email"]

    }

def clientes_schema(users) -> list:
    return [cliente_schema(user) for user in users]
def colegio_schema(colegio) -> dict:
    return {
        "id" : str(colegio["_id"]),
       "name": colegio["name"],
       "distrito" : colegio["distrito"],
       "tipo" : colegio["tipo"],
       "direccion": colegio["direccion"]

    }

def colegios_schema(colegios) -> list:
    return [colegio_schema(colegio) for colegio in colegios]
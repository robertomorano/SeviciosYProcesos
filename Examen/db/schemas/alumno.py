def alumno_schema(alumno) -> dict:
    return {
        "id" : str(alumno["_id"]),
       "name": alumno["name"],
       "surname" : alumno["surname"],
       "birth_date" : alumno["birth_date"],
       "curso": alumno["curso"],
       "repetidor": alumno["repetidor"],
       "id_colegio": alumno["id_colegio"]

    }

def alumnos_schema(alumnos) -> list:
    return [alumno_schema(alumno) for alumno in alumnos]
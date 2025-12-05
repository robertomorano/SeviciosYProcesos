from fastapi import FastAPI, APIRouter , HTTPException
from db.models.cliente import Cliente


router = APIRouter(prefix="/clientes", tags=["clientes"])




lista_cliente = [Cliente(id = 1, dni = "202043Y",name= "Paco", surname= "Peres", phone= 15, email="a@b.c"),
              Cliente(id = 2, dni = "202043Y",name= "Pacdasdas", surname= "Peres", phone= 15, email="a@b.c"), 
              Cliente(id = 3, dni = "202043Y",name= "Paadsadaco", surname= "Peres", phone= 15, email="a@b.c")]


def next_id():
    return (max(lista_cliente, key=id).id+1)


def find_cliente(id : int):
    cliente = [cliente for cliente in lista_cliente if cliente.id == id]
    return cliente[0] if (len(cliente) !=0) else {"Esta": "Mal"}

#GET Method

@router.get("/")
def cliente():
    return lista_cliente

@router.get("/{id_cliente}")
def get_cliente(id_cliente: int):
    cliente = [cliente for cliente in lista_cliente if cliente.id == id_cliente]
    return cliente[0] if (len(cliente) !=0) else {"Esta": "Mal"}

@router.get("/")
def cliente(id : int):
    return find_cliente(id)


#POST Method

@router.post("/", status_code=201, response_model=Cliente)
def add_cliente(cliente: Cliente):
    cliente.id = next_id()
    lista_cliente.append(cliente)
    return cliente

#PUT Method

@router.put("/{id}", status_code=200, response_model=Cliente)
def modify_cliente(id:int, cliente:Cliente):    
    for index, saved_clliente in enumerate(lista_cliente):
        if saved_clliente.id == id:
            cliente.id=id
            lista_cliente[index] = cliente
            return cliente

    raise HTTPException(status_code=404, detail="cliente not found")

#DELETE Method

@router.delete("/{id}")
def delete_cliente(id:int):
    print("dadw")
    for saved_clliente in lista_cliente:
        print(saved_clliente)
        if saved_clliente.id == id:
            lista_cliente.remove(saved_clliente)
            return {}
    raise HTTPException(status_code=404, detail="cliente not found")
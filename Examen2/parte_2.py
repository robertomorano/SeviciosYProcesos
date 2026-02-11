from multiprocessing import Process, Queue

def proceso_1(dept_buscado, cola_salida):
    try:
        with open("salarios.txt", "r") as f:
            for linea in f:
                partes = linea.strip().split(";")
                if len(partes) == 4:
                    nombre, apellido, salario, dept = partes
                    if dept.lower() == dept_buscado.lower():
                        cola_salida.put((nombre, apellido, salario))
    except FileNotFoundError:
        pass
    cola_salida.put(None)

def proceso_2(salario_min, cola_entrada, cola_salida):
    while True:
        datos = cola_entrada.get()
        # Primero comprobamos si es None, luego desempaquetamos
        if datos is None:
            break
        
        nombre, apellido, salario = datos
        if int(salario) >= salario_min:
            cola_salida.put(datos)
            
    cola_salida.put(None)

def proceso_3(cola_entrada):
    with open("empleados.txt", "w") as f:
        while True:
            datos = cola_entrada.get()
            if datos is None:
                break
            
            nombre, apellido, salario = datos
            f.write(f"{apellido} {nombre}, {salario}\n")

def main():
    dept = input("Introduce el nombre del departamento: ")
    try:
        min_sal = int(input("Introduce el salario mínimo: "))
    except ValueError:
        return

    q1_a_2 = Queue()
    q2_a_3 = Queue()

    p1 = Process(target=proceso_1, args=(dept, q1_a_2))
    p2 = Process(target=proceso_2, args=(min_sal, q1_a_2, q2_a_3))
    p3 = Process(target=proceso_3, args=(q2_a_3,))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    

if __name__ == "__main__":
    main()
from multiprocessing import Process, Queue
import time

# Esta función es el CONSUMIDOR (recibe datos)
def sumar_desde_cola(cola):
    suma = 0
    while numero != None:
        
        numero = cola.get() 
        
            
        suma += numero
        print(f"[Proceso {time.perf_counter()}] Suma parcial: {suma}")
    
    print(f"Resultado final: {suma}")


def leer_archivo_y_enviar(ruta, cola):
    try:
        with open(ruta, "r") as f:
            for linea in f:
                n = int(linea.strip())
                print(f"Enviando {n} a la cola...")
                cola.put(n)
                
    except FileNotFoundError:
        print("Archivo no encontrado.")
    finally:
        # IMPORTANTE: Avisar que hemos terminado
        cola.put(None)

def main():
    qiu = Queue()
    
    # Creamos el archivo de prueba
    with open("ej3.txt", "w") as f:
        f.write("10\n20\n30")

    # Definimos los procesos
    # p1 leerá y p2 sumará
    p1 = Process(target=leer_archivo_y_enviar, args=("ej3.txt", qiu))
    p2 = Process(target=sumar_desde_cola, args=(qiu,))

    inicio = time.perf_counter()
    
    p1.start()
    p2.start()

    p1.join() # Esperamos a que termine de leer
    p2.join() # Esperamos a que termine de sumar

    fin = time.perf_counter()
    print(f"Todo terminado en {fin - inicio:.4f} segundos")

if __name__ == "__main__":
    main()
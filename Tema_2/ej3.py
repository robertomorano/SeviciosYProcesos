from multiprocessing import Process, Queue
import time
import os


def sumar(number : int) -> None:
    suma = 0
    for i in range(number):
        suma += i
        print(suma)
    print("Ej terminado")

def leer():
    try:
        with open("ej3.txt", "r") as ej:
            for linea in ej:
                pass
    except FileNotFoundError:
        print("adwa")

        

def main():

    qiu = Queue()
    #dEClara proceso nombre y los argumentos a pasar
    p1 = Process(target=sumar, args=(qiu,))
    p2 = Process(target=sumar, args=(qiu,))
    #inicia el subproceso distinto al main
    inicio = time.perf_counter()
    p1.start()
    p2.start()
    print("Se hace print antes de terminar p")
    #Esperar a que acabe el subproceso para continuar ejecutando
    p1.join()
    qiu.put(None)
    p2.join
    fin = time.perf_counter()
    tiempo = fin-inicio
    print(f"Procesos terminado, {tiempo}")

if __name__ == "__main__":
    main()
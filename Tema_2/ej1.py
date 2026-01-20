from multiprocessing import Process, Pool
import time
import os


def sumar(number : int) -> None:
    suma = 0
    for i in range(number):
        suma += i
        print(suma)
    print("Ej1 terminado")



def main():
    with Pool(processes=3) as pool:
        numbers = [10,20,30,50]
        inicio = time.perf_counter()
        results = pool.map(sumar, numbers)
        fin = time.perf_counter()
    tiempo = fin-inicio   
    print(results)
    print(f"Proceso terminado, {tiempo}")


    #dEClara proceso nombre y los argumentos a pasar
    p = Process(target=sumar, args=(9,))
    #inicia el subproceso distinto al main
    inicio = time.perf_counter()
    p.start()

    print("Se hace print antes de terminar p")
    #Esperar a que acabe el subproceso para continuar ejecutando
    p.join()
    fin = time.perf_counter()
    tiempo = fin-inicio
    print(f"Proceso terminado, {tiempo}")

if __name__ == "__main__":
    main()
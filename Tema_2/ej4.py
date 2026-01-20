from multiprocessing import Process, Pipe
import time


def sumar(number : int) -> None:
    suma = 0
    for i in range(number):
        suma += i
        print(suma)
    print("Ej terminado")

def leer(send):
    send.send()


def main():

    send, rec = Pipe()
    #dEClara proceso nombre y los argumentos a pasar
    p1 = Process(target=leer, args=(send,))
    p2 = Process(target=sumar, args=(rec,))
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
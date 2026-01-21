from multiprocessing import Process, Pipe
import time


def leer_archivo_y_enviar(ruta, send):
    try:
        with open(ruta, "r") as f:
            for linea in f:
                n = int(linea.strip())
                print(f"Enviando {n} otro proceso")
                send.send(n)
                
    except FileNotFoundError:
        print("Archivo no encontrado.")
    finally:
        
        send.send(None)

def sumar(rec ) -> None:
    number = rec.recv()
    suma = 0
    while number is not None:
        print(f"numero recibudo: {number}")
        suma += number

        print(suma)
        number = rec.recv()
    print("Ej terminado")



def main():
    with open("ej3.txt", "w") as f:
        f.write("10\n20\n30")

    send, rec = Pipe()
    #dEClara proceso nombre y los argumentos a pasar
    p1 = Process(target=leer_archivo_y_enviar, args=("ej3.txt",send))
    p2 = Process(target=sumar, args=(rec,))
    #inicia el subproceso distinto al main
    inicio = time.perf_counter()
    p1.start()
    p2.start()
    print("Se hace print antes de terminar p")
    #Esperar a que acabe el subproceso para continuar ejecutando
    p1.join()
    
    p2.join()
    fin = time.perf_counter()
    tiempo = fin-inicio
    print(f"Procesos terminado, {tiempo}")

if __name__ == "__main__":
    main()
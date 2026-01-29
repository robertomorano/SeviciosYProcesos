from multiprocessing import Process, Queue
import time
import os


def proceso1_filtrar_peliculas(ruta_fichero, anio, queue):
 
  
        print(f"Leyendo fichero: {ruta_fichero}")
        print(f"Filtrando películas del año {anio}...")
        
        peliculas_enviadas = 0
        
        with open(ruta_fichero, 'r', encoding='utf-8') as f:
            for linea in f:
                linea = linea.strip()
                if not linea:
                    continue
                
                # Separar nombre y año por punto y coma
                partes = linea.split(';')
                if len(partes) == 2:
                    nombre_pelicula = partes[0].strip()
                    anio_estreno = partes[1].strip()
                    
                    # Filtrar por año
                    if anio_estreno == str(anio):
                        queue.put((nombre_pelicula, anio_estreno))
                        peliculas_enviadas += 1
                        print(f"Enviada: {nombre_pelicula} ({anio_estreno})")
        
        # Enviar señal de finalización
        queue.put((None, None))
        
        print(f"\nFinalizado - Películas enviadas: {peliculas_enviadas}")
        



def proceso2_guardar_peliculas(queue, anio):

    nombre_fichero = f"peliculas{anio}.txt"
    
    print(f"\nEsperando películas para guardar en {nombre_fichero}")
    
    peliculas_recibidas = 0
    
    with open(nombre_fichero, 'w', encoding='utf-8') as f:
        while True:
            pelicula, anio_estreno = queue.get()
            

            if pelicula is None:
                break
            

            f.write(f"{pelicula};{anio_estreno}\n")
            peliculas_recibidas += 1
            print(f"Guardada: {pelicula}")
    
    print(f"\nFinalizado - Películas guardadas: {peliculas_recibidas}")
    print(f"Fichero creado: {nombre_fichero}")


def main():
    anio_actual = 2026
    anio = None
    
    while anio is None:
        try:
            entrada = input(f"\nIntroduce un año (menor a {anio_actual}): ").strip()
            anio = int(entrada)
            
            if anio >= anio_actual:
                print(f" El año debe ser menor a {anio_actual}")
                anio = None
            elif anio < 1800:
                print(" Por favor, introduce un año válido")
                anio = None
                
        except ValueError:
            print(" Por favor, introduce un número válido")
    
        ruta_fichero = 'peliculas.txt'
    
    

    tiempo_inicio = time.time()
    

    queue = Queue()
    
    # Crear los procesos
    p1 = Process(target=proceso1_filtrar_peliculas, args=(ruta_fichero, anio, queue))
    p2 = Process(target=proceso2_guardar_peliculas, args=(queue, anio))
    

    p1.start()
    p2.start()
    
    # Esperar a que terminen
    p1.join()
    p2.join()
    
    tiempo_fin = time.time()
  

    fichero_salida = f"peliculas{anio}.txt"
    if os.path.exists(fichero_salida):
        print(f"Contenido de {fichero_salida}:")
        
        with open(fichero_salida, 'r', encoding='utf-8') as f:
            contenido = f.read()
            if contenido:
                print(contenido)
            else:
                print(f"(No se encontraron películas del año {anio})")
    
    


if __name__ == '__main__':
    main()
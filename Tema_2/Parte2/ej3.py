

from multiprocessing import Process, Pool
import random
import time
import os


def proceso1_generar_notas(ruta_fichero):

    notas = [round(random.uniform(1.0, 10.0), 2) for _ in range(6)]
    
    with open(ruta_fichero, 'w', encoding='utf-8') as f:
        for nota in notas:
            f.write(f"{nota}\n")
    
    return ruta_fichero


def proceso2_calcular_media(args):

    ruta_fichero, nombre_alumno = args
    
    try:
        with open(ruta_fichero, 'r', encoding='utf-8') as f:
            notas = [float(linea.strip()) for linea in f if linea.strip()]
        
        if notas:
            media = sum(notas) / len(notas)
            

            with open('medias.txt', 'a', encoding='utf-8') as f:
                f.write(f"{media:.2f} {nombre_alumno}\n")
            
            return (nombre_alumno, media)
        else:
            return (nombre_alumno, 0.0)
            
    except Exception as e:
        print(f"Error procesando {nombre_alumno}: {e}")
        return (nombre_alumno, 0.0)


def proceso3_encontrar_maxima():

    try:
        with open('medias.txt', 'r', encoding='utf-8') as f:
            lineas = f.readlines()
        
        if not lineas:
            return
        
        nota_maxima = -1
        alumno_maxima = ""

        for linea in lineas:
            partes = linea.strip().split()
            if len(partes) >= 2:
                nota = float(partes[0])
                alumno = partes[1]
                
                print(f"{alumno}: {nota:.2f}")
                
                if nota > nota_maxima:
                    nota_maxima = nota
                    alumno_maxima = alumno
        

    except FileNotFoundError:
        print("Error: No se encontró el fichero medias.txt")
    except Exception as e:
        print(f"Error al buscar la nota máxima: {e}")


def ejercicio_con_pool():

    
    # Limpiar medias.txt si existe
    if os.path.exists('medias.txt'):
        os.remove('medias.txt')
    
    tiempo_inicio = time.time()
    

    
    ficheros = [f'Alumno{i+1}.txt' for i in range(10)]
    
    with Pool(processes=10) as pool:
        pool.map(proceso1_generar_notas, ficheros)
    

    
    argumentos = [(f'Alumno{i+1}.txt', f'Alumno{i+1}') for i in range(10)]
    
    with Pool(processes=10) as pool:
        resultados = pool.map(proceso2_calcular_media, argumentos)
    

    proceso3_encontrar_maxima()
    
    tiempo_fin = time.time()
    tiempo_total = tiempo_fin - tiempo_inicio
    
    print(f"\n⏱️  Tiempo total de ejecución: {tiempo_total:.4f} segundos\n")


def ejercicio_con_bucles():

    
    # Limpiar medias.txt si existe
    if os.path.exists('medias.txt'):
        os.remove('medias.txt')
    
    tiempo_inicio = time.time()
    

    
    procesos = []
    for i in range(10):
        p = Process(target=proceso1_generar_notas, args=(f'Alumno{i+1}.txt',))
        procesos.append(p)
        p.start()
    
    # Esperar a que todos terminen
    for p in procesos:
        p.join()
    
    
    procesos = []
    for i in range(10):
        p = Process(target=proceso2_calcular_media, 
                   args=((f'Alumno{i+1}.txt', f'Alumno{i+1}'),))
        procesos.append(p)
        p.start()
    
    # Esperar a que todos terminen
    for p in procesos:
        p.join()
    
    
    proceso3_encontrar_maxima()
    
    tiempo_fin = time.time()
    tiempo_total = tiempo_fin - tiempo_inicio
    

if __name__ == '__main__':

    
    
    
    opcion = input("\nSelecciona una opción (1/2/3): ").strip()
    
    if opcion == '1':
        ejercicio_con_pool()
    elif opcion == '2':
        ejercicio_con_bucles()
    elif opcion == '3':
        ejercicio_con_pool()
        time.sleep(1)
        ejercicio_con_bucles()
    else:

        ejercicio_con_pool()
    
   
    for i in range(10):
        try:
            os.remove(f'Alumno{i+1}.txt')
        except:
            pass
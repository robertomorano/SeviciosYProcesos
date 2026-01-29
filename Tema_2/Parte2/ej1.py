from multiprocessing import Pool
from pathlib import Path


def contar_vocal(vocal, archivo):
    
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            texto = f.read().lower()  # Convertir a minúsculas para contar todas las vocales
        
        # Contar la vocal
        cantidad = texto.count(vocal.lower())
        
        return (vocal, cantidad)
    
    except FileNotFoundError:
        print(f"Error: El archivo {archivo} no existe")
        return (vocal, 0)
    except Exception as e:
        print(f"Error al procesar {vocal}: {e}")
        return (vocal, 0)


def main():
    # Archivo a procesar
    archivo = "vocales.txt"
    
    
    
    
    # Vocales a contar
    vocales = ['a', 'e', 'i', 'o', 'u']
    
    # Crear un pool de procesos
    with Pool(processes=5) as pool:
        # Preparar los argumentos para cada proceso
        # Usamos starmap para pasar múltiples argumentos
        argumentos = [(vocal, archivo) for vocal in vocales]
        
        # Lanzar los procesos en paralelo
        resultados = pool.starmap(contar_vocal, argumentos)
    
    # Imprimir los resultados
    
    print("CONTADOR DE VOCALES EN PARALELO")
    
    print(f"Archivo analizado: {archivo}\n")
    
    total_vocales = 0
    for vocal, cantidad in resultados:
        print(f"Vocal '{vocal}': {cantidad} apariciones")
        total_vocales += cantidad
    
    
    print(f"Total de vocales: {total_vocales}")
    


if __name__ == "__main__":
    main()
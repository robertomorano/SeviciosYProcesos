import multiprocessing
import random 
def proceso_1(fecha):
    
   """ with open (f"{fecha}.txt", "w") as file:
        for i in range(20):
            file.write(random.randint(0,21))
            file.write(".")
            decimal = random.randint(0,99)
            print(decimal)
            if(decimal<10):
                file.write(f"0")
            file.write(decimal)"""
   with open(f"{fecha}.txt", "w") as file:
        # Generamos 24 números y los unimos con ";"
        temps = [str(random.randint(-5, 40)) for _ in range(24)]
        file.write(";".join(temps))


            



def proceso_2(fecha):
        with open(f"{fecha}.txt", "r") as file:
            # Leemos, separamos y convertimos a entero para ordenar bien
            contenido = file.read()
            temperaturas = [int(t) for t in contenido.split(";") if t]
            temperaturas.sort()
            
            # El máximo es el último elemento
            maxima = temperaturas[-1]
            
        with open("maximas.txt", "a") as f_max:
            f_max.write(f"{fecha}: {maxima}\n")

def proceso_3(fecha):
    with open(f"{fecha}.txt", "r") as file:
            # Leemos, separamos y convertimos a entero para ordenar bien
            contenido = file.read()
            temperaturas = [int(t) for t in contenido.split(";") if t]
            temperaturas.sort()
            
            # El máximo es el último elemento
            maxima = temperaturas[0]
            
    with open("minimas.txt", "a") as f_max:
        f_max.write(f"{fecha}: {maxima}\n")
def main():
    procesos_fase_1 = []
    procesos_fase_2 = []

    
    for dia in range(1, 32):
        p = multiprocessing.Process(target=proceso_1, args=(dia,))
        procesos_fase_1.append(p)
        p.start()

    
    for p in procesos_fase_1:
        p.join()

    
    for dia in range(1, 32):
        p_max = multiprocessing.Process(target=proceso_2, args=(dia,))
        p_min = multiprocessing.Process(target=proceso_3, args=(dia,))
        
        procesos_fase_2.extend([p_max, p_min])
        
        p_max.start()
        p_min.start()

    
    for p in procesos_fase_2:
        p.join()

    


if __name__ == "__main__":
    main()
import random

#Crea una lista de enteros de longitud 10 que se inicializará con números aleatorios comprendidos entre 1 y 100. 

def listRandom():
    return [random.randint(1,101) for x in range(10)]

#Crea un programa que pida diez números reales por teclado, los almacene en una lista,
# y luego lo recorra para averiguar el máximo y mínimo y mostrarlos por pantalla.

def listMaxMin():
    list = [input("Dame numero") for x in range(10)]
    print(max(list))
    print(min(list))

# Realiza un programa que pida 8 números enteros y los almacene en una lista.
#  A continuación, recorrerá esa tabla y mostrará esos números junto con la
#  palabra “par” o “impar” según proceda.

def evenOdd():
    list = [input("Dame numero") for x in range(8)]
    for num in list:
        if num%2==0:
            print(num, "Even")
        else:
            print(num, "Odd")


# Escribe un programa que lea 10 números por teclado y
#  que luego los muestre ordenados de mayor a menor.

def Order():
    list = sorted([input("Dame numero") for x in range(10)])
    print(list)

# Crea un programa que cree una lista de enteros de tamaño 100 
# y lo rellene con valores enteros aleatorios entre 1 y 10. 
# Luego pedirá un valor N y mostrará cuántas veces aparece N.
def Ej5():
    list = [random.randint(1,11) for x in range(100)]
    user = int(input("numeraco aqui"))
    cont = 0
    for num in    

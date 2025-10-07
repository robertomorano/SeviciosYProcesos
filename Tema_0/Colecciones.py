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
    #numberlist = [1,2,3,4,5,6,7,8,9,10]
    dicti = {"1": 0,"2": 0,"3": 0,"4": 0,"5": 0,"6": 0,"7": 0, "8": 0, "9": 0, "10": 0}
    for i in range(len(dicti)):
        for num in list:
            if num == (i+1):
                cont+=1
        dicti[i+1] = cont
        cont = 0
                


# Escribe un programa que tome una cadena de texto
# como entrada y genere un diccionario que cuente la frecuencia de cada palabra en el texto.

def frequency():
    alphabet = {}
    string = "asdaefgmgmaigpm"
    string.count("a")
    for letter in string:
        cont = string.count(letter)
        alphabet[letter] = cont
    
    print(alphabet)

# Crea un programa que permita al usuario agregar, eliminar y buscar contactos en una 
# libreta de direcciones implementada como un diccionario. La clave del diccionario será 
# el nombre del contacto y el valor, su número de teléfono.
#  Crea un menú para las distintas opciones e implementa una función para cada opción.

def contact():
    contacts = {}
    option = int(input(''' Menu
                       1. Agregar
                       2.Eliminar.
                       3.Buscar
                       0.Salir'''))

    while(option != 0):
        if (option == 1):
            nombre = input("NombrePersona")
            contacts[nombre] =  int(input("NumeroPersona"))
        elif (option == 2):
            nombre = input("NombrePersona")
            contacts.pop(nombre)

        elif (option == 3):
            nombre = input("NombrePersona")
            print(nombre, "->",contacts[nombre])
        option = int(input(''' Menu
                       1. Agregar
                       2.Eliminar.
                       3.Buscar
                       0.Salir'''))

        
#   Diseña un programa que registre las ventas de una tienda en un diccionario, 
# donde las claves son los nombres de
#  los productos y los valores son las cantidades vendidas.
#  El programa debe permitir al usuario agregar
#  nuevas ventas y calcular el total de ventas para un producto específico. 
# Implementa un menú con ambas opciones. 

#lo mismo de arriba pero sumando

"""
Crea un diccionario donde las claves son las letras del abecedario y los valores, 
la puntuación para cada letra, como en el Scrabble.
 El programa le pedirá una palabra al usuario y 
 se mostrará por pantalla la puntuación que tiene la palabra en total.
"""

#rea un diccionario donde las claves sean el conjunto 1 de la siguiente tabla y los valores, el conjunto 2:
# El programa debe pedir una frase al usuario y debe mostrar la frase encriptada. 
# Para ello, cada vez que encuentre en la frase una letra del conjunto 1
#  la sustituirá por su correspondiente en el conjunto 2.
def crytography():
    encrypt = {"e":"p", "i":"v","k": "i", "m": "u", "p": "m", "q":"t","r":"e","s":"r","t":"k","u":"q", "v":"s"}
    normal = input("Texto aqui")
    encrypted = ""
    for letter in normal:
        if letter in encrypt.keys:
            encrypted += encrypt[letter]
        else:
            encrypted += letter
    print (encrypted)

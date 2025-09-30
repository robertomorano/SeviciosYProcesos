import math
import random


def parImpar(n):
    if n%2==0:
        print("par")
    else:
        print("impar")

def ordenar(n1,n2):
    if n1>n2:
        print(n1,n2)
    else:
        print(n2,n1)
"""
Escribe un programa que vaya pidiendo al usuario números enteros positivos que debe ir sumando. 
Cuando el usuario no quiera insertar más números, inroducirá
un número negativo y el algoritmo, antes de acabar, 
mostrará la suma de los números positivos introducidos por el usuario.

"""
def sumar():
    array = []
    num = 0
    sum = 0
    while (num >= 0):
        num = int(input("Un numero"))
        array.append(num)
    
    for number in array:
        sum+=number 
    print(sum)

"""
Codificar el juego “el número secreto”, que consiste en acertar un número
entre 1 y 100 (generado aleatoriamente). Para ello se introduce por teclado una serie de números, 
para los que se indica: “mayor” o “menor”, según sea mayor 
o menor con respecto al número secreto. El proceso termina cuando el usuario
acierta o cuando se rinde (introduciendo un -1).
"""
def secret_num_game():
    secret_num = random.randint(1,100)
    num = int(input("Un numero"))
    while(num!=-1):
        if(num==secret_num):
            print("Hasacertado")
            num = -1
        elif(num<secret_num):
            print("Es menor")
            num = int(input("Un numero"))
        else:
            print("Es mayor:(")
            num = int(input("Un numero"))
        
"""
Escribir una aplicación para aprender a contar, que pedirá un número n y mostrará todos los números del 1 al n.
"""    
def contar():
    limite =  int(input("Un numero"))
    for i in range(limite):
        print(i)

"""
Pedir un número y calcular su factorial.
Por ejemplo, el factorial de 5 se denota 5! y es igual a 5x4x3x2x1 = 120.
"""

def factorial():
    num = int(input("Un numero"))
    fcto = 1
    for i in range (1, num+1):
        fcto *= i
    print(fcto)

#Realiza un programa que pida un número entero positivo y nos diga si es primo o no.
def primo():
    num = int(input("Un numero"))
    cont = 2
    primo = True
    while(num%cont != 0 and cont<=math.sqrt(num)):
        cont +=1
        


def main():
    print("hola")
if __name__=="__main__":
    main()

"""
Solicita al usuario un número n y dibuja 
un triángulo de base y altura n. Por ejemplo para n=4 debe dibujar lo siguiente:
   *
  * *
 * * *
* * * *

"""
def triangulo():
    n = int(input("Un numero"))
    tri = ""
    for i in range(1,n+1):
        tri += " "*((n+1)-i) + "* "

"""
Escribe una función a la que se le pasen dos enteros 
y muestre todos los números comprendidos entre ellos. 
Desde el método main() lee los dos números enteros, 
los cuales deben introducirlos el usuario, y pásalos como parámetros de entrada de la función.

"""


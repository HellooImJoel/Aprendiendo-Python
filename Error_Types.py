### Error Types ###


"""
Analizar el tipo de error que nos está lanzado el codigo, y evaluar la forma de solucionarlo.
- Que error a dado?
- Por qué lo ha dado?
- Como podemos solucionarlo?
"""

# SyntaxError

#print "Hola buenas a todos!"        | el error se produce porque faltan los parentesis.

print("Hola buenas a todos!!")


# NameError

# print(language)    | la variable 'language' no esta definida.

language = "Spanish"
print(language)


# IndexError

my_list = ["Python", "Swift", "Kotlin", "Dart", "JavaScript"]
print(my_list[0])
print(my_list[4])
print(my_list[-1])
#print(my_list[5])  | el indice de la lista está fuera del rango de la lista.


# MoluleNotFoundError

#import maths   |  el nombre del modulo es incorrecto, por tanto, no se encuentra el modulo deseado.
import math


# AttributeError

#print(math.PI)    |  error en la forma de acceder a un atributo.
print(math.pi)  


# KeyError

my_dict = {"Nombre":"Joel", "Apellido":"Stadelman", "Edad":"23", 1:"Python"}

print(my_dict["Edad"])
#print(my_dict["Apelido"])    | se produce al llamar de forma erronea una key
print(my_dict["Apellido"]) 


# TypeError

#print(my_list["Nombre"])    | el error surge debido a que el indice de la lista debe ser un entero y se le esta pasando un string.
print(my_list[0])


# ImportError

#from math import PI
from math import pi
print(pi)

# ValueError

#my_int = int("10 Años")   | son es posible transformar un str en int.
my_int = int("10")
print(my_int)


# ZeroDivisionError

print(4/2)
#print(4/0)  | division entre cero









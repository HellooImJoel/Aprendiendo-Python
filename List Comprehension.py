# Lis Comprehension


"""
List comprehension in Python is a compact way of creating a list from a sequence. 
It is a short way to create a new list. List comprehension is considerably faster than processing 
a list using the for loop.
"""

# zipeando listas, es decir, comprimiendo una estructura de datos(list)

my_original_list = [0,1,2,3,4,5,6,7]
print(my_original_list)

my_range = range(8)
print(list(my_range))

my_list = [i + 1 for i in range(8)]  
print(my_list)

my_list = [i * 2 for i in range(8)]  
print(my_list)

def sum_five(number):
    return number + 5

my_list = [sum_five(i) * i for i in range(8)]  
print(my_list)

# esto permite crear una lista de forma rapida y donde se puede ir modificando a medida que se va creando.
# pueden aplicarse funciones o lo que sea necesario para realizar dichas modificaciones.
# el punto clave es que "se esta modificando un valor antes de guardarlo."





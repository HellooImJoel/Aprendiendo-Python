# Tuples

"""
A tuple is a collection of different data types which is ordered and unchangeable (immutable). Tuples are written with round brackets, (). Once a tuple is created, we cannot change its values. We cannot use add, insert, remove methods in a tuple because it is not modifiable (mutable). Unlike list, tuple has few methods. Methods related to tuples:

tuple(): to create an empty tuple
count(): to count the number of a specified item in a tuple
index(): to find the index of a specified item in a tuple
operator: to join two or more tuples and to create a new tuple
"""

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (23, 1.92, "Joel", "Stadelman", "Joel")
my_other_tuple = (35, 60, 23, 77, 31, 23)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
# print(my_tuple[-6])  IndexError

print(my_tuple.count("Joel"))
print(my_tuple.index("Stadelman"))
print(my_tuple.index("Joel"))

"""
my_tuple[1] = 1.95
print(my_tuple) 

Una tupla es inmutable, una vez definidos los valores estos no pueden modificarse.
"""
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

"""
por definicion una tupla es inmutable, si se quiere que sea mutable, 
entonces es mejor utilizar una 'lista'.
"""
my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "Joel"
my_tuple.insert(1, "Amarillo")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

# esto es un ejemplo de como realizar una modificacion a la tupla
# cuanto mas inmutables los datos mejor.

del my_tuple # 'del' borra directamente todo el elemento.
print(my_tuple) # NameError: name 'my_tuple' is not defined.











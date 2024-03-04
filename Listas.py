# Listas
"""
There are four collection data types in Python :

List: is a collection which is ordered and changeable(modifiable). Allows duplicate members.
Tuple: is a collection which is ordered and unchangeable or unmodifiable(immutable). Allows duplicate members.
Set: is a collection which is unordered, un-indexed and unmodifiable, but we can add new items to the set. Duplicate members are not allowed.
Dictionary: is a collection which is unordered, changeable(modifiable) and indexed. No duplicate members.
"""

my_list = list()
my_other_list = [] 

print(len(my_list))

my_list = [23, 35, 52, 30, 30, 24, 67]
print(my_list)
print(len(my_list))

my_other_list = [23, 1.92, "Joel", "Stadelman"]
print(my_other_list)
print(type(my_other_list))

# cuando tenemos una lista podemos acceder a los elementos dentro de esta, cada uno por separado o de la forma que sea necesaria.

# operaciones simples con listas

print(my_other_list[0]) # se puede acceder a un elemento especifico de la lista indicando la posicion del elemento, esto se hace mediante el index de la lista.
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
#print(my_other_list[4]) IndexError: list index out of range
#print(my_other_list[-5]) IndexError: list index out of range

print(my_other_list.count("Joel"))  
print(my_list.count(30))  
# En este caso 'count' aplicado a una lista retorna el numero de occurrencias de un valor en la lista.

age, height, name, surname = my_other_list
print(name)

age, height, name, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(name)

print(my_list + my_other_list) # concatenamos dos listas



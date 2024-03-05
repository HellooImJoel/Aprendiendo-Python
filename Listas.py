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

my_list = "Hola python"
print(my_list)
print(type(my_list)) # una forma de ver el tipado dinamico(debilmente tipado), anteriormente 'my_list' era una variable tipo lista y ahora se cambió a una variable de tipo string.

"""
"en Python no se pueden crear constantes", pero se pueden crear variables finales, es decir,
una buena practica para definir una variable como 'constante' es escribir dicha variable en MAYUSCULAS,
de este modo quien opere con el codigo puede identificar dichas variables, esto es una regla no escrita.
"""

# Slicing Items from a List

"""
Positive Indexing: We can specify a range of positive indexes by specifying the start, 
end and step, the return value will be a new list. 
(default values for start = 0, end = len(lst) - 1 (last item), step = 1)
"""

fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4] # it returns all the fruits
# this will also give the same result as the one above
all_fruits = fruits[0:] # if we don't set where to stop it takes all the rest
orange_and_mango = fruits[1:3] # it does not include the first index
orange_mango_lemon = fruits[1:]
orange_and_lemon = fruits[::2] # here we used a 3rd argument, step. It will take every 2cnd item - ['banana', 'mango']

"""
Negative Indexing: We can specify a range of negative indexes by specifying the start, 
end and step, the return value will be a new list.
"""

fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:] # it returns all the fruits
orange_and_mango = fruits[-3:-1] # it does not include the last index,['orange', 'mango']
orange_mango_lemon = fruits[-3:] # this will give starting from -3 to the end,['orange', 'mango', 'lemon']
reverse_fruits = fruits[::-1] # a negative step will take the list in reverse order,['lemon', 'mango', 'orange', 'banana']


# Operando con listas

my_other_list.append("GST.inc")
print(my_other_list)

my_other_list.insert(1, "amarillo")
print(my_other_list)

my_other_list.remove("amarillo")
print(my_other_list)

my_pop_element = fruits.pop() # la funcion 'pop' desapila el ultimo elemento.
print(my_pop_element)
print(fruits)

del fruits[2] # elimina el elemento de la posicion indicada.
print(fruits)

my_new_list = fruits.copy()

fruits.clear()
print(fruits)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list = ['orange', 'banana', 'mango', 'lemon']
print(my_new_list)
my_new_list.sort()
print(my_new_list)


# Sublistas

print(my_new_list[1:3]) # conociendo el indice se pueden hacer sublistas.


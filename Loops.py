# Loops\bucles\ciclos

"""
        >> Loops <<

Life is full of routines. In programming we also do lots of repetitive tasks. 
In order to handle repetitive task programming languages use loops. 
Python programming language also provides the following types of two loops:

- while loop
- for loop
"""

"""
        >> While Loop <<

We use the reserved word while to make a while loop. 
It is used to execute a block of statements repeatedly until a given condition is satisfied. 
When the condition becomes false, the lines of code after the loop will be continued to be executed.

# syntax
while condition:
    code goes here
"""

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2 
else:      # es opcional
    print("Mi condicion es mayor o igual que 10") # Al 'While' se le puede agregar una condicion utilizando 'else' para cuando el bucle termine.

print("La ejecucion continua")


while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecucion")
        break    # Break: We use break when we like to get out of or stop the loop.
    print(my_condition)


print("El bucle ha terminado")

print("##############################################")

"""
        >> For Loop <<

A for keyword is used to make a for loop, similar with other programming languages, 
but with some syntax differences. Loop is used for iterating over a sequence 
(that is either a list, a tuple, a dictionary, a set, or a string).

- For loop with list

# syntax
for iterator in lst:
    code goes here
"""
my_list = [23, 35, 52, 30, 30, 24, 67]

for element in my_list:   # El bucle 'for' se ejecuta tantas veces como elementos tenga la lista.
    print(element) 

print("-----------------------------------------")
my_tuple = (23, 1.92, "Joel", "Stadelman", "Joel")

for element in my_tuple:
    print(element)

print("-----------------------------------------")
my_set = {"Joel", "Stadelman", 23}

for element in my_set:
    print(element)

print("-----------------------------------------")
my_dict = {
            'Nombre':"Joel",
            'Apellido':"Stadelman", 
            'Edad':23, 
            'Lenguajes':{"Python", "Swifit", "Kotlin"},
            1:1.92
            }

for element in my_dict:
    print(element)
    if element == "Edad":
        continue
    print("esto se ejecuta")
else:
    print("EL bucle 'for' para mi diccionario ha terminado")



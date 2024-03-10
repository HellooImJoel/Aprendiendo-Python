# Conditionals

"""
By default, statements in Python script are executed sequentially from top to bottom. 
If the processing logic require so, the sequential flow of execution can be altered in two way:

Conditional execution: a block of one or more statements will be executed if a certain expression is true.

Repetitive execution: a block of one or more statements will be repetitively executed as long as a certain 
expression is true. In this section, we will cover if, else, elif statements. The comparison and logical 
operators we learned in previous sections will be useful here.
"""

# los 'condicionales' son la manera de establecer un flujo de trabajo en nuestro codigo, 
#decidir si alguna parte debe ejecutarse o no.


"""
        >> 'If' Conditional <<

In python and other programming languages the key word 'if' is used to check if 
a condition is true and to execute the block code. Remember the indentation after the colon.

# syntax
if condition:
    this part of code runs for truthy conditions
"""

my_condition = False

if my_condition:  
    print("Se ejecuta la condicion del if")


print("La ejecucion continua")


my_condition = 5*2

if my_condition == 10:  
    print("Se ejecuta la condicion del segundo if")


"""
        >> If Else <<

If condition is true the first block will be executed, if not the else condition will run.

# syntax
if condition:
    this part of code runs for truthy conditions
else:
    this part of code runs for false conditions
"""
my_condition = 5*2

if my_condition > 10 and my_condition < 20:  
    print("Es mayor que 10 y menor que 20")
else:
    print("Es menor o igual que 10 o igual que 20")

"""
        >> If Elif Else <<

In our daily life, we make decisions on daily basis. 
We make decisions not by checking one or two conditions but multiple conditions. 
As similar to life, programming is also full of conditions. We use elif when we have multiple conditions.

# syntax
if condition:
    code
elif condition:
    code
else:
    code
"""

print("##################################################")

my_condition = 5*5

if my_condition > 10 and my_condition < 20:  
    print("Es mayor que 10 y menor que 20")
elif my_condition == 25:
    print("Es igual a 25")
else:
    print("Es menor o igual que 10 o igual que 20 o distinto de 25")



my_string = ""   # Si tenemos un string vacio lo concidera como 'False'

if not my_string:
    print("mi cadena de texto es vacia")

if my_string == "Mi cadena de texto":
    print("mi cadena de texto no es vacia")






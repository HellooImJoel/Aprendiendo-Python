# Functions

"""
        >> Functions <<

So far we have seen many built-in Python functions. In this section, 
we will focus on custom functions. What is a function? Before we start making functions, 
let us learn what a function is and why we need them?

Defining a Function
A function is a reusable block of code or programming statements designed to perform a certain task. 
To define or declare a function, Python provides the def keyword. The following is the syntax 
for defining a function. The function block of code is executed only if the function is called or invoked.

Declaring and Calling a Function
When we make a function, we call it declaring a function. 
When we start using the it, we call it calling or invoking a function. 
Function can be declared with or without parameters.

# syntax
# Declaring a function
def function_name():
    codes
    codes
# Calling a function
function_name()
"""

def my_function():
    print("Esto es una funcion")

my_function()

def sum_two_values(first_value, second_value):
    print(first_value + second_value)

sum_two_values(7, 5)
sum_two_values(73256, 52435)
sum_two_values("5","7")
sum_two_values(1.4, 5.2)


def sum_two_values_with_return(first_value, second_value):
    my_sum = first_value + second_value
    return my_sum


#my_result = sum_two_values(1.4, 5.2)
#print(my_result)

my_result = sum_two_values_with_return(3,4)
print(my_result)


def print_name(name, surname):
    print(f"{name} {surname}")

print_name(surname = "Stadelman",name = "Joel") # Es posible reordenar los parametros que ingresan dado que no se respete el orden en el que se quiere mostrar.

"""
        >> Function with Default Parameters <<

Sometimes we pass default values to parameters, when we invoke the function. 
If we do not pass arguments when calling the function, their default values will be used.

# syntax
# Declaring a function
def function_name(param = value):
    codes
    codes
# Calling function
function_name()
function_name(arg)
"""


def print_name_with_default(name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Joel", "stadelman", "Grandote")
print_name_with_default("Joel", "stadelman")


def print_texts(*texts):
    for text in texts:
        print(text)

print_texts("Hola")
print_texts("Hola", "Python", "GrayScallet")

def print_upper_texts(*texts):
    for text in texts:
        print(text.upper())

print_upper_texts("Hola")
print_upper_texts("Hola", "Python", "GrayScallet")










## Higher Order Functions ##

"""
In Python functions are treated as first class citizens, allowing you to perform the following operations on functions:

- A function can take one or more functions as parameters.
- A function can be returned as a result of another function.
- A function can be modified.
- A function can be assigned to a variable.

In this section, we will cover:

- Handling functions as parameters.
- Returning functions as return value from another functions.
- Using Python closures and decorators.
"""

# Function as a Parameter

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def  sum_two_values_and_add_value(first_value, second_value, f):
    return f(first_value + second_value)

print(sum_two_values_and_add_value(5,2,sum_one)) 
print(sum_two_values_and_add_value(5,2,sum_five)) 



def sum_numbers(nums):  # normal function
    return sum(nums)    # a sad function abusing the built-in sum function :<

def higher_order_function(f, lst):  # function as a parameter
    summation = f(lst)
    return summation
result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)       # 15


# Function as a Return Value

def square(x):          # a square function
    return x ** 2

def cube(x):            # a cube function
    return x ** 3

def absolute(x):        # an absolute value function
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type): # a higher order function returning a function
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = higher_order_function('square')
print(result(3))       # 9
result = higher_order_function('cube')
print(result(3))       # 27
result = higher_order_function('absolute')
print(result(-3))      # 3





# Python Closures

"""
Python allows a nested function to access the outer scope of the enclosing function. 
This is is known as a Closure. Let us have a look at how closures work in Python. 
In Python, closure is created by nesting a function inside another encapsulating function 
and then returning the inner function.
"""


def add_ten(original_value):
    val = 10
    def add(num):
        return num + val + original_value
    return add

closure_result = add_ten(1)
print(closure_result(5))  # 15
print((add_ten(5))(1))




# Built-in Higher Order Functions

# Map
"""
La funcion map necesita un elemento iterable (listas,tuplas...)

Syntax

    map(function, iterables) 
"""

def multiply_two(number):
    return number * 2


number = [2, 5, 10, 21, 30]

print(list(map(multiply_two ,number)))
print(list(map(lambda number: number * 2 ,number)))


# Filter

def fil_greater_than_ten(number):
    if number > 10:
        return True
    return False


print(list(filter(fil_greater_than_ten, number)))
print(list(filter(lambda number: number > 10 ,number)))


# Reduce

from functools import reduce

def sum_two_values(first_value, second_value):
    return first_value + second_value


print(reduce(sum_two_values, number))


"""
la funcion "reduce" reduce todos los elementos del iterable a un valor unico, es similar a una sumatora.
"""


word = ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']

print(reduce(sum_two_values, word))











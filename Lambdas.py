## Lambdas ##

"""
las Lambdas son un tipo de funciones con una particularidad quue las diferencia del resto.
Se trata de funciones anonimas, es decir, son funciones que no tienen nombre.

Syntax

lambda arguments : expression
"""

# una lambda se puede almacenar en una variable

sum_two_values = lambda first_value, second_value: first_value + second_value
print(sum_two_values(1,3))

multiply_values = lambda first_value, second_value: first_value * second_value -3
print(multiply_values(2,4))


def sum_three_values(value): 
    return lambda first_value, second_value: first_value + second_value + value

print(sum_three_values(5)(2,4))
















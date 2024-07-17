### Regular Expressions ###

# Las expresiones regulares son un mecanismo esteandar para todos los lenguajes que permite
# inspeccionar si en un determinado string existen ciertos elementos.
# Utilizando este metodo podemos verificar la existencia de los elementos y obtener el numero de ocurrencias
# de lo que coincide con la expresion regular.

"""
Methods in re Module
To find a pattern we use different set of re character sets that allows to search for a match in a string.

re.match(): searches only in the beginning of the first line of the string and returns matched objects if found, else returns None.
re.search: Returns a match object if there is one anywhere in the string, including multiline strings.
re.findall: Returns a list containing all matches
re.split: Takes a string, splits it at the match points, returns a list
re.sub: Replaces one or many matches within a string

"""

import re

my_string = "Esta es la leccion numero 7: Expresiones Regulares"
my_other_string = "Esta no es la leccion numero 6: Manejo de Ficheros"

#print(re.match("Esta es la leccion", my_string, re.I))
#print(re.match("Esta es la leccion", my_other_string))
#print(re.match("Expresiones Regulares", my_string))


match = re.match("Esta es la leccion", my_string, re.I)
print(match)
start, end = match.span()
print(my_string[start:end])


match = re.match("Esta no es la leccion", my_other_string, re.I)
# if not(match == None): # Otra forma de comprobar el None
# if match != None: # Otra forma de comprobar el None
if match is not None:
    print(match)
    start, end = match.span()
    print(my_other_string[start:end])






















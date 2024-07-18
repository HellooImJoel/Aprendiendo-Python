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

my_string = "Esta es la leccion numero 7: Leccion llamada Expresiones Regulares"
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


## search

search = re.search("leccion", my_string, re.I)
print(search)
start, end = search.span()
print(my_string[start:end])


## findall

findall = re.findall("leccion", my_string, re.I)
print(findall)

my_new_string = "leccion, Leccion, LEccion, LECcion, LECCion,LECCión, LECCIon, LECCIOn, LECCION, LECCiÓN"

findall = re.findall("[l|L][e|E][c|C][c|C][i|I][o|ó|O|Ó][n|N]", my_new_string, re.I)
print(findall)

## split

split = re.split(":", my_string)
print(split)


## sub

sub = re.sub("Expresiones Regulares","RegEx", my_string)
print(sub)

sub = re.sub("[l|L]eccion","LECCION", my_string)
print(sub)



## Patterns

pattern = r'[lL]eccion'
print(re.findall(pattern, my_string))

pattern = r'[lL]eccion|Expresiones'
print(re.findall(pattern, my_string))

pattern = r'[a-z]'
print(re.findall(pattern, my_string))

pattern = r'[0-9]'
print(re.findall(pattern, my_string))

pattern = r"\d"
print(re.findall(pattern, my_string))

pattern = r"\D"
print(re.findall(pattern, my_string))

pattern = r"[l].*"
print(re.findall(pattern, my_string))

email = "gonzalezstadelmanjoel@gmail.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+$"
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))

email = "joeldevv@joeldev.com.ar"
print(re.findall(pattern, email))

# Strings

my_string = "Mi String"
my_other_string = "Mi otro String"

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con salto de linea"
print(my_tab_string)

my_scape_string = "\\Este es un String \\n escapado"
print(my_scape_string)


# formateo

name, surname, age = "Joel", "Stadelman", 23

print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))

# utilizar 'format' es muy util al momento de internacionalizar el texto, es decir, 
#que el texto se muentre en diferentes idiomas sin necesidad de estar repitiendo codigo 
#en cada uno de los idiomas.

print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Desempaquetado de caracteres
language = "python"
a, b, c, d, e, f = language
print(a)
print(b) 

# Division

language_slice = language[1:3] # toma desde el caracter en la posicion 1 hasta el de la posicion 3 sin imprimirlo, ya que 3 es el limite.
print(language_slice)

language_slice = language[1:] # # toma desde el caracter en la posicion 1 hasta el final del string ya que no se le indica ningun limite.
print(language_slice)

language_slice = language[0:6:2] # Salta partes del string y asi se puede mostrar por partes sin modificar el string en su totalidad.
print(language_slice)

# Reverse

reversed_language = language[::-1]
print(reversed_language)


# Funciones

print(language.capitalize()) # capitalize(): Converts the first character of the string to capital letter
print(language.upper())  # return a copy of the string converted to uppercase
print(language.count("t")) # count(): returns occurrences of substring in string, count(substring, start=.., end=..). The start is a starting indexing for counting and end is the last index to count.
print(language.isnumeric()) # isnumeric(): Checks if all characters in a string are numbers or number related (just like isdigit(), just accepts more symbols, like ½)
print(language.lower()) # return a copy of the string converted to lowercase
print(language.upper().isupper()) # isupper(): Checks if all alphabet characters in the string are uppercase

# startswith(): Checks if String Starts with the Specified String
challenge = 'thirty days of python'
print(challenge.startswith('thirty')) # True

challenge = '30 days of python'
print(challenge.startswith('thirty')) # False

# endswith(): Checks if a string ends with a specified ending
challenge = 'thirty days of python'
print(challenge.endswith('on'))   # True
print(challenge.endswith('tion')) # False


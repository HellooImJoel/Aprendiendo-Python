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


# Dicts

"""
A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.
"""

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {'Nombre':"Francisco", 'Apellido':"Gonzalez", 'Edad':23, 1:1.92}

my_dict = {
            'Nombre':"Joel",
            'Apellido':"Stadelman", 
            'Edad':23, 
            'Lenguajes':{"Python", "Swifit", "Kotlin"},
            1:1.92
            }

print(my_other_dict)
print(my_dict)

# En un diccionario se pueden guardar datos con la estructura 'clave:valor'.

print(len(my_other_dict))
print(len(my_dict))

print(my_dict['Nombre'])

my_dict['Nombre'] = "Joel F."
print(my_dict['Nombre'])

print(my_dict[1])

my_dict['Calle'] = "GrayScallet 629"
print(my_dict)

del my_dict['Calle']
print(my_dict)

print("Joel F." in my_dict)
print("Apellido" in my_dict)
print(my_dict['Apellido'])

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_list = ['Nombre', 1, 'Piso']

my_new_dict = my_dict.fromkeys(my_list)    # Se crea un diccionario nuevo, pero que no tiene valores asignados.
print(my_new_dict)

my_new_dict = my_dict.fromkeys(('Nombre', 1, 'Piso'))   
print(my_new_dict)

my_new_dict = my_dict.fromkeys(my_dict)    
print(my_new_dict)

"""
Esta es una buena forma de utilizar 'fromkeys' ya que es posible crear un nuevo diccionario reutilizando 
las clave que tiene otro ya creado, de este modo se puede guardar otros valores.
"""






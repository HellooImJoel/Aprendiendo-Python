# Variable

my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# Concatenación de variables en un print
print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print("El valor es:", my_bool_variable)

# Algunas funciones de sistema
print(len(my_string_variable)) # 'len()' cuenta los caracteres de un string, inclusio los espacios.

# Variables en una sola línea
name, surname, alias, age = "Joel", "Stadelman", "Grandote", 23
print("Me llamo",name, surname,"tengo", age, "anios de edad","y mi alias es", alias)
print(type(age))

# Inputs
"""
name = input("What is your name:")
age = input("How old are you:")
"""
print(name)
print(age)

# Cambiamos su tipo
name = 23
age = "Joel"

print(name)
print(age)

# Forzamos el tipo?  en los 'input' es bueno utilizar esto, ya que restringimos a que el dato que ingresa sea del tipo que queremos.
address: str = "Mi direccion"
address: int = 32
print(address)



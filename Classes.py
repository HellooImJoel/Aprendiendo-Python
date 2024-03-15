# Classes

"""
Classes and Objects
Python is an object oriented programming language. 
Everything in Python is an object, with its properties and methods. 
A number, string, list, dictionary, tuple, set etc. used in a program 
is an object of a corresponding built-in class. We create class to create an object. 
A class is like an object constructor, or a "blueprint" for creating objects. 
We instantiate a class to create an object. The class defines attributes and the behavior of the object, 
while the object, on the other hand, represents the class.
"""


class MyEmtyPerson:     # Por convencion, los nombres de las clases se escriben con la primera letra en mayusculas, sin  espacios y sin guiones.
    pass          # 'pass' evita errores, ya que permite que la clase sea vacia y el codigo se ejecute.(es solo un ejemplo, si se da el caso de una clase vacia, entonces se debe reconciderar si en realidad es necesario definir dicha clase) 
                  # In Python programming, the pass statement is a null statement which can be used as a placeholder for future code.

print(MyEmtyPerson)
print(MyEmtyPerson())

# las clases deben tener 'constructores', dicho constructor de alguna manera debe poder recibir parametros.

"""
class Person:
    def __init__(self) -> None:
        pass

# The self variable represents the instance of the object itself.
# The __init__ method is roughly what represents a constructor in Python. 
"""

class Person:
    def __init__(self, name, surname, alias = "Sin alias"):
        self.full_name = f"{name} {surname} ({alias})" # propiedad publica.
        self.__name = name            # propiedad privada.
        self.__surname = surname      # Declarar una variable con el formato '__variablename' establece que dicha variable es privada, es decir, que no se puede acceder a su valor directamente fuera de la clase, para ello es necesario defenir un 'getter'. 

    def get_name(self):
        return self.__name      # esta es una buena forma de definir un 'getter', lo que permite devolver el valor de la variable, pero no se puede modificar el mismo, para ello es necesario definir un 'setter'.

    def walk(self):
        print(f"{self.full_name} esta caminando")

my_person = Person("Joel", "Stadelman")
print(my_person.full_name)
my_person.walk()

my_other_person = Person("Joel", "Stadelman", "GrayScallet")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Agus Korell (Pana rabbit)"
print(my_other_person.full_name)







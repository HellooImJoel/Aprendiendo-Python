# Exception Handling

"""
Python uses try and except to handle errors gracefully. A graceful exit (or graceful handling) 
of errors is a simple programming idiom - a program detects a serious error condition and "exits gracefully", 
in a controlled manner as a result. Often the program prints a descriptive error message to a terminal 
or log as part of the graceful exit, this makes our application more robust. 
The cause of an exception is often external to the program itself. An example of exceptions could be an 
incorrect input, wrong file name, unable to find a file, a malfunctioning IO device. 
Graceful handling of errors prevents our applications from crashing.
"""

"""
Es necesario tener mecanismos de manejo de errores, para cuando surjan dichos errores 
la aplicacion/programa no detenga su funcinamiento por completo.
"""

numberOne = 5
numberTwo = 1
numberTwo = "1"

# try-except

try:
    print(numberOne + numberTwo)
    print("No se ha produciodo un error")
except:
    print("Se ha produciodo un error")


# try-except-else

try:
    print(numberOne + numberTwo)
    print("No se ha produciodo un error")
except:
    print("Se ha produciodo un error")
else:
    print("La ejecucion continua correctamente") # esto se ejecuta solamente si no se produce una excepcion.
finally: 
    print("La ejecucion continua")   # 'finally' se ejecuta siempre.


"""
try:
    {Run this code}
except: --> "may or may not have a condition"
    {Excecute this code when there is an exception}
else:
    {No exception? Run this code}
finally:
    {Always run this code}
"""

try:
    print(numberOne + numberTwo)
    print("No se ha produciodo un error")
except ValueError:
    print("Se ha produciodo un ValueError")
except TypeError:
    print("Se ha produciodo un TypeError")

# teniendo esto claro, podemos especializar las excepciones, de forma que se ejecute un codigo en especifico dependiendo el tipo de error que se haya producido.


# Captura la informacion de la excepcion
try:
    print(numberOne + numberTwo)
    print("No se ha produciodo un error")
except ValueError as error:
    print(error)
except Exception as error: # 'Exception' representa una excepcion general
    print(error)







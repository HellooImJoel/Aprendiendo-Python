#Operadores


calc1 = 3+4
print(calc1)

calc2 = 3-4
print(calc2)

calc3 = 3*4
print(calc3)

calc4 = 3/4
print(calc4)

calc5 = 18%2  #operador de modulo
print(calc5) 

calc6 = 18//5 #operador 'Floor division'
print(calc6) 

calc7 = 2**3
print(calc7) #operador exponente

# Tambien se puede usar con strings
print("Hello "+"Python") 
# No se puede operar con tipos diferentes, pero de pueden usar las funciones del sistema para cambiar el tipo de datos
print("El valor es:"+ str(5)) 

# Los simbolos se pueden combinar entre ellos
calc8 = 2**3 + 3 - 7 / 1 // 4
print(calc8)

print("hola " * 5) # en este caso el string se puede escribir tantas veces como el valor del numero entero lo indique
# pero solo se puede hacer con numeros 'enteros'.

my_float = 2.5 * 2
print("hola " * int(my_float))

# operadores de comparacion

calc9 = 3 > 4
print(calc9)

calc10 = 3 < 4
print(calc10)

calc11 = 3 >= 4
print(calc11)

calc12 = 3 <= 4
print(calc12)

calc13 = 3 == 4
print(calc13)

calc14 = 3 != 4
print(calc14)

calc15 = (3 > 4 > 2)
print(calc15)


# Cuando tenemos strings lo que se hace es una comparacion por orden alfabetico.
# Las mayusculas y minusculas afectan al resultado ya que se trata de una ordenacion por ASCII.

calc16 = ("Hola" > "Python")
print(calc16)

calc17 = ("Hola" < "Python")
print(calc17)

calc18 = ("Hola" >= "Python")
print(calc18)

calc19 = ("Hola" <= "Python")
print(calc19)

calc20 = ("Hola" == "Python")
print(calc20)

calc21 = ("Hola" != "Python")
print(calc21)


# Operadores logicos

print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 > 4 or ("Hola" > "Python" and 4 == 4))
print(not(3 > 4))


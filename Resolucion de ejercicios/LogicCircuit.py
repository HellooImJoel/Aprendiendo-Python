# Logic Circuit 


from sympy import symbols
from sympy.logic.boolalg import Or, And, Not
from sympy.logic.inference import satisfiable
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.visualization import plot_bloch_multivector
#from qiskit import Aer, execute
import matplotlib.pyplot as plt

def dibujar_circuito(expresion):
    # Crear los registros cuánticos y clásicos
    q = QuantumRegister(4, 'q')
    c = ClassicalRegister(4, 'c')

    # Crear el circuito cuántico
    circuito = QuantumCircuit(q, c)

    # Añadir las puertas lógicas al circuito en función de la expresión booleana
    if isinstance(expresion, And):
        circuito.ccx(q[0], q[1], q[2])
    elif isinstance(expresion, Or):
        circuito.cx(q[0], q[2])
        circuito.cx(q[1], q[2])
        circuito.ccx(q[0], q[1], q[2])
    elif isinstance(expresion, Not):
        circuito.x(q[0])

    # Medir el resultado
    circuito.measure(q, c)

    # Dibujar el circuito
    circuito.draw(output='mpl')
    plt.show()

# Definir los símbolos
x, y, z = symbols('x y z')

# Crear una expresión booleana
expresion = Or(And(x, Not(y)), And(Not(x), y), And(And(x, Not(y), Not(z)), And(Not(x), y, z)), Not(y))

# Dibujar el circuito
dibujar_circuito(expresion)






















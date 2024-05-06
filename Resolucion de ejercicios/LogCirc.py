from sympy import symbols, Or, And, Not

# Definir las variables
x, y, z = symbols('x y z')

# Definir la expresión booleana
expr = Or(x & Not(y) | Not(x) & y | (x & Not(y) & Not(z) | Not(x) & y & z) | y)

# Crear la tabla de verdad
truth_table = []
for i in range(2):
    for j in range(2):
        for k in range(2):
            truth_table.append((i, j, k))

# Evaluar la expresión booleana para cada combinación de valores de verdad
for combination in truth_table:
    x_val, y_val, z_val = combination
    result = expr.subs({x: x_val, y: y_val, z: z_val})
    print(f"For x={x_val}, y={y_val}, z={z_val}, result={result}")

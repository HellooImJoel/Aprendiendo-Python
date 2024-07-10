import numpy as np
import matplotlib.pyplot as plt

# Define the function and points
x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x)

# Tangent line (horizontal line at y = 1)
tangent_y = np.ones_like(x) * 1

# Points
x_points = [np.pi / 2, 2 * np.pi / 3]
y_points = [1, np.sin(2 * np.pi / 3)]

# Secant line
secant_x = np.array([np.pi / 2, 2 * np.pi / 3])
secant_y = np.array([1, np.sin(2 * np.pi / 3)])

plt.figure(figsize=(10, 6))
plt.plot(x, y, label="f(x) = sin(x)")
plt.plot(x, tangent_y, '--', label="Tangent line at x=π/2")
plt.plot(secant_x, secant_y, 'ro-', label="Secant line")

# Plot points
plt.scatter(x_points, y_points, color='red')

# Labels and legend
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Graph of f(x) = sin(x) with Tangent and Secant Lines")
plt.legend()
plt.grid(True)
plt.show()

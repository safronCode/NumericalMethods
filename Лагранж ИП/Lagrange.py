import sympy
import matplotlib.pyplot as plt
import numpy as np

# Initial conditions
nodeX = [-1.5, -0.75, 0, 0.75, 1.5]
nodeY = [-1, 5, -10, -5, 4]

# The function returns the coefficients
def lcoefs(X, symbol):
    coefs = []
    for i in range(0, len(X)):
        coef = 1
        for j in range(0, len(X)):
            if i != j:
                coef *= (symbol - X[j]) / (X[i] - X[j])

        coefs.append(coef)
    return coefs


# The function returns the polynomial
def lpoly(coefs, Y):
    lagrange = 0
    for k in range(0, len(Y)):
        lagrange += nodeY[k] * coefs[k]
    return lagrange


x = sympy.Symbol('x')
lagrangePoly = lpoly(lcoefs(nodeX, x), nodeY)
f = sympy.lambdify(x, lagrangePoly)

x_vals = np.linspace(min(nodeX) - 10, max(nodeX) + 10, 500)
y_vals = f(x_vals)

# plotting the graph
plt.plot(x_vals, y_vals, color='green', label='Lagrange IP')
plt.scatter(nodeX, nodeY, color='red', label='Interpolation Nodes')

# setting up the graph
plt.xlabel('X')
plt.ylabel('Y')
plt.xlim(min(nodeX) - 10, max(nodeX) + 10)
plt.ylim(min(nodeY) - 10, max(nodeY) + 10)
plt.title('Lagrange Interpolation Polynomial with Points')
plt.legend()
plt.grid(True)

plt.show()

print("\t*Initial conditions:")
for index in range(0, len(nodeX)):
    print(f"point ( {nodeX[index]} ; {nodeY[index]} )")
print(f"\n\t*The Lagrange interpolation polynomial looks like this:\n{lagrangePoly.simplify()}")

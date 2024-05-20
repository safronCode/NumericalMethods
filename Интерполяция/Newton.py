import sympy
import numpy as np
import matplotlib.pyplot as plt

# The function returns the split difference
def split_difference(x_coord, y_coord):
    if len(x_coord) == 1 and len(y_coord) == 1:
        result = y_coord[0]
        return result
    elif len(x_coord) == 2 and len(y_coord) == 2:
        result = (y_coord[1] - y_coord[0]) / (x_coord[1] - x_coord[0])
        return result
    else:
        return (split_difference(x_coord[1:], y_coord[1:]) - split_difference(x_coord[:-1], y_coord[:-1])) / (
                    x_coord[-1] - x_coord[0])

# The function returns newton polynomial
def npoly(x_coord, y_coord, symbol):
    newtoon = split_difference(x_coord[0:1], y_coord[0:1])
    for i in range(2, len(x_coord) + 1):
        element = split_difference(x_coord[0:i], y_coord[0:i])
        for j in range(0, i - 1):
            element *= (symbol - x_coord[j])
        newtoon += element
    return newtoon
if __name__ == "__main__":

    # Initial conditions
    nodeX = [-5, -2, 0, 1, 2, 3]
    nodeY = [-32, 22, 0, -11, 11, 1]

    if len(nodeX) != len(nodeY):
        print("The number of X coordinates does not match with Y coordinates :(")
        exit()

    x = sympy.Symbol('x')
    newtonPoly = npoly(nodeX, nodeY, x).simplify()
    f = sympy.lambdify(x, newtonPoly)

    x_vals = np.linspace(min(nodeX) - 10, max(nodeX) + 10, 500)
    y_vals = f(x_vals)

    # plotting the graph
    plt.plot(x_vals, y_vals, color='green', label='Newton IP')
    plt.scatter(nodeX, nodeY, color='red', label='Interpolation Nodes')

    # setting up the graph
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.xlim(min(nodeX) - 10, max(nodeX) + 10)
    plt.ylim(min(nodeY) - 10, max(nodeY) + 10)
    plt.title('Newton Interpolation Polynomial with Points')
    plt.legend()
    plt.grid(True)

    plt.show()

    print("\t*Initial conditions:")

    for index in range(0, len(nodeX)):
        print(f"point ( {nodeX[index]} ; {nodeY[index]} )")
    print(f"\n\t*The Newton interpolation polynomial looks like this:\n{newtonPoly}")

import matplotlib.pyplot as plt
import sympy


# The function calculates the x-points and the y-points placed by them
def eiler(start_stop, koshi, step, symbols, f):

    # Load symbols and elements with index 0
    sym_x = symbols[0]
    sym_y = symbols[1]
    x_list = [start_stop[0]]
    y_list = [koshi[1]]

    # Using the method, we fill the arrays with x-points and y-points
    for i in range(1, int((abs(start_stop[1] - start_stop[0]) / step) + 1)):
        x_list.append(x_list[i - 1] + step)
        y_list.append(y_list[i - 1] + step * f.subs({sym_x: x_list[i - 1], sym_y: y_list[-1]}))

    # Outputting values to the terminal
    print(f" y\'= F(x,y)\t:\ty\'= " + sympy.pretty(f) + "\n",
          f"Cauchy problem: y(x) = something\t:\t y({koshi[0]}) = {koshi[1]}\n",
          f"Start position: {start_stop[0]}\tStop postion: {start_stop[1]}\tStep: {step}\n\n"
          f""
          f"{'Index':<5}|{'x':>5}{'|':>5}{'y':>5}\n",
          "=" * 26)
    for index in range(len(x_list)):
        print(f"{index:<5}|{x_list[index]:>8.4f} |{y_list[index]:>10.4f}")
    print("\n" * 3)

    return x_list, y_list


# The function draws the integral curve
def plotting(x, y, f):
    plt.plot(x, y, marker='o', label='Euler Method')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Numerical Solution using Euler Method')
    plt.grid(True)
    equation_text = f"$y' = {sympy.latex(f)}$"
    plt.text(1, 1, equation_text, fontsize=12, ha='right', va='top', transform=plt.gca().transAxes)
    plt.show()


if __name__ == "__main__":
    # Enter your symbols
    x_sym, y_sym = sympy.symbols('x y')

    # Enter step
    h = 0.4

    # Enter x range of change
    range_values = [2.6, 4.8]

    # Enter f(x,y):   y' = f(x,y)
    func = y_sym / x_sym - 1

    # Enter the Cauchy problem: y(x_0) = Cauchy[1], x_0 = Cauchy[0]
    cauchy = [2.6, 1]

    x_vals, y_vals = eiler(range_values, cauchy, h, [x_sym, y_sym], func)
    plotting(x_vals, y_vals, func)

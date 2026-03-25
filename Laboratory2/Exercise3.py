import numpy as np
import matplotlib.pyplot as plot
import math

# Taylor Approximations Functions
def taylor_sin(x, n):
    res = 0
    for i in range(n):
        res += ((-1)**i * x**(2*i + 1)) / math.factorial(2*i + 1)
    return res

def taylor_cos(x, n):
    res = 0
    for i in range(n):
        res += ((-1)**i * x**(2*i)) / math.factorial(2*i)
    return res



# Printint (Plotting) functions
def print_comparison(f1, f2, namef1, namef2, n=5, color_a="blue", color_b="orange"):
    x = np.linspace(-np.pi, np.pi, 100)

    plot.figure(figsize=(10, 6))

    plot.plot(x, f1(x), label=namef1, color=color_a)
    plot.plot(x, f2(x, n), label=namef2, color=color_b)

    plot.title(f'Comparison {namef1} vs {namef2} (n={n})')
    plot.xlabel('Time')
    plot.ylabel('Amplitude')
    plot.grid(True, which='both')
    plot.axhline(y=0, color='k')
    plot.legend() # add a legend
    
    plot.show()

def print_function(f, name, n=5, color="green", y_axis_scale=0):
    x = np.linspace(-np.pi, np.pi, 100)

    plot.figure(figsize=(10, 6))

    plot.plot(x, f(x, n), label=name, color=color)

    plot.title(f'Comparison {name} (n={n})')
    plot.xlabel('Time')
    plot.ylabel('Amplitude')
    plot.grid(True, which='both')
    plot.axhline(y=0, color='k')

    if y_axis_scale == 1:
        plot.ylim(-0.01, 0.01)
    elif y_axis_scale == 2:
        plot.ylim(-0.05, 0.05)
    else:
        plot.ylim(0.5, 1.5)
    
    plot.show()



# Difference Functions and Formulas
def diff_sin(x, n):
    return taylor_sin(x, n) - np.sin(x)

def diff_cos(x, n):
    return taylor_cos(x, n) - np.cos(x)

def formula(x, n):
    # sin²(x) + cos²(x)
    return taylor_sin(x, n)**2 + taylor_cos(x, n)**2

def formula2(x, n):
    # sin²(x) + cos²(x) - 1
    return taylor_sin(x, n)**2 + taylor_cos(x, n)**2 - 1


# Main Programm
print_comparison(np.sin, taylor_sin, "sin", "Taylor sin", n=2)
print_comparison(np.cos, taylor_cos, "cos", "Taylor cos", n=2)
print_function(diff_sin, "difference of sine and taylor approx", n=2, y_axis_scale=1)
print_function(diff_cos, "difference of cos and taylor approx" , n=2, y_axis_scale=1)
print_function(formula, "sin²(x) + cos²(x)", n=2)
print_function(formula2, "Taylor series : sine and cosine", n=2, y_axis_scale=2)
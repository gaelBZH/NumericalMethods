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
def print_comparison(f1, f2, namef1, namef2, n=5):
    x = np.linspace(-np.pi, np.pi, 100)

    plot.figure(figsize=(10, 6))

    plot.plot(x, f1(x), label=namef1, color="blue")
    plot.plot(x, f2(x, n), label=namef2, color="orange")

    plot.title(f'Comparison {namef1} vs {namef2} (n={n})')
    plot.xlabel('Time')
    plot.ylabel('Amplitude')
    plot.grid(True, which='both')
    plot.axhline(y=0, color='k')
    plot.legend() # add a legend
    
    plot.show()

def print_function(f, name, n=5, color="green", limited=False):
    x = np.linspace(-np.pi, np.pi, 100)

    plot.figure(figsize=(10, 6))

    plot.plot(x, f(x, n), label=name, color=color)

    plot.title(f'Comparison {name} (n={n})')
    plot.xlabel('Time')
    plot.ylabel('Amplitude')
    plot.grid(True, which='both')
    plot.axhline(y=0, color='k')

    if limited:
        plot.ylim(-0.01, 0.01)
    else:
        plot.ylim(0.5, 1.5)
    
    plot.show()



# Difference Functions
def diff_sin(x, n):
    return taylor_sin(x, n) - np.sin(x)

def diff_cos(x, n):
    return taylor_cos(x, n) - np.cos(x)

def formula(x, n):
    # sin²(x) + cos²(x)
    return taylor_sin(x, n)**2 + taylor_cos(x, n)**2



# Main Programm
print_comparison(np.sin, taylor_sin, "sin", "Taylor sin", n=2)
print_comparison(np.cos, taylor_cos, "cos", "Taylor cos", n=2)
print_function(diff_sin, "difference of sine and taylor approx", n=2, limited=True)
print_function(diff_cos, "difference of cos and taylor approx" , n=2, limited=True)
print_function(formula, "sin²(x) + cos²(x)", n=2)
# Numerical Methods - Laboratory 2
### Gaël KERNINON (Erasmus Student)

## Exercise 1
#### a. Calculating number of possible numbers.
- k (1 bit), so $k \in \{0, 1\}$
- $d_1d_2$ (2 bits), so  $d_1d_2 \in \{00, 01, 10, 11\}$
- e is 2 bits (0, 1, 2 or 3), so $e-1 \in \{-1, 0, 1, 2\}$

By calculating, we have $2 \times 4 \times 4 = 32$ possible real numbers represented in this system.

#### b. Calculating Maximum Number.
The maximum number is positive ($k=0$), mantissa is $m=0.11_2 = 0.75_{10}$ and $e = 11_2 = 3_{10}$, so we have :
$$
rd(x)_{maximum} = (-1)^0 \times 0.75 \times 2^{(3-1)} = 3.0
$$
#### c. Calculating smallest positive number
The smallest positive number is, of course, positive ($k=0$), mantissa is $m = 0.01_2 = 0.25_{10}$ and $e=0$, so we have :
$$
rd(x)_{minimum} = (-1)^0 \times 0.25 \times 2^{(0-1)} = 0.125
$$


## Exercise 2
```py
import numpy as np

def exercise_2(precision, p):
    n = 0
    while True:
        epsilon = precision(1 / 2**n)
        if precision(1.0) + epsilon == precision(1.0):
            print(f"Precision float{p} : n={n} and epsilon = 1/2**{n}")
            break
        n += 1

exercise_2(np.float16, 16)
exercise_2(np.float32, 32)
exercise_2(np.float64, 64)
# exercise_2(np.float128, 128) does not exist (!)
```
output :
```
Precision float16 : n=11 and epsilon = 1/2**11
Precision float32 : n=24 and epsilon = 1/2**24
Precision float64 : n=53 and epsilon = 1/2**53
```

## Exercise 3
```py
import numpy as np
import matplotlib.pyplot as plot
import math

# Taylor Approximations Functions
def taylor_sin(x, n):
    res = 0
    for n in range(n):
        res += ((-1)**n * x**(2*n + 1)) / math.factorial(2*n + 1)
    return res

def taylor_cos(x, n):
    res = 0
    for n in range(n):
        res += ((-1)**n * x**(2*n)) / math.factorial(2*n)
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

def print_function(f, name, n=5, color="green"):
    x = np.linspace(-np.pi, np.pi, 100)

    plot.figure(figsize=(10, 6))

    plot.plot(x, f(x, n), label=name, color=color)

    plot.title(f'Comparison {name} (n={n})')
    plot.xlabel('Time')
    plot.ylabel('Amplitude')
    plot.grid(True, which='both')
    plot.axhline(y=0, color='k')
    
    plot.show()



# Difference Functions
def diff_sin(x, n):
    return np.sin(x) - taylor_sin(x, n)

def diff_cos(x, n):
    return np.cos(x) - taylor_cos(x, n)

def formula(x, n):
    # sin²(x) + cos²(x) - 1
    return taylor_sin(x, n)**2 + taylor_cos(x, n)**2 - 1



# Main Programm
print_comparison(np.sin, taylor_sin, "sin", "Taylor sin", n=2)
print_comparison(np.cos, taylor_cos, "cos", "Taylor cos", n=2)
print_function(diff_sin, "difference of sine and taylor approx", n=5)
print_function(diff_cos, "difference of cos and taylor approx", n=5)
print_function(formula, "sin²(x) + cos²(x) - 1", n=5)
```
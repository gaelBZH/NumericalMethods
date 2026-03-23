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

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
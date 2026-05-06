import numpy as np
import matplotlib.pyplot as plt

def f(x):
   return np.sin(4*x)*x

# Defining derivative of function
def g(x):
   return np.sin(4*x) + 4*np.cos(4*x)*x

# Implementing Newton Method with 3 Stopping Criterias
def newton(x0, tolx, tolf, nmax):
   """
   Returns (root, step) 
   """
   step = 1

   # Criteria 1: n <= n_max
   while step <= nmax: 
      if g(x0) == 0.0:
         raise ZeroDivisionError(f"g({x0=})=0.0 ({step=})")
      
      x1 = x0 - f(x0)/g(x0)
      
      # Criteria 2 and 3: TOLX and TOLF
      if abs(x1 - x0) <= tolx or abs(f(x1)) <= tolf:
         return x1, step
      
      x0 = x1
      step += 1
      
   # Non convergent after nmax iterations
   return None, nmax

if __name__ == "__main__":
   x0 = float(input('Enter Guess: '))
   tolx = float(input('TOLX (Error on x): '))
   tolf = float(input('TOLF (Error on f(x)): '))
   nmax = int(input('Maximum Step: '))
   
   root, iterations = newton(x0, tolx, tolf, nmax)

   if root is not None:
      print(f"Root: {root}, Iterations: {iterations}")
   else:
      print("Did not converge.")

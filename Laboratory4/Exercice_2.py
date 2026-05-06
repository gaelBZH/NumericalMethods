import numpy as np
from Exercice_1 import *

TOLX = 1e-6
TOLF = 1e-6
NMAX = 50

roots_found = []
iterations_needed = []
valid_guesses = []

# Loop with different initial points
for x0 in np.linspace(-2.0, 2.0, 500):
    root, steps = newton(x0, TOLX, TOLF, NMAX)
    if root is not None:
        roots_found.append(root)
        iterations_needed.append(steps)
        valid_guesses.append(x0)

# Results
plt.figure(figsize=(12, 5))
colors = ["blue", "red"]

# Graph 1
plt.subplot(1, 2, 1)
plt.scatter(valid_guesses, roots_found, s=5, c=colors[0], alpha=0.6)
plt.title("Root found depending on the initial Guess")
plt.xlabel("Initial Guess (x0)")
plt.ylabel("Converged Root")
plt.grid(True, linestyle='--', alpha=0.7)

# Graph 2
plt.subplot(1, 2, 2)
plt.plot(valid_guesses, iterations_needed, c=colors[1], alpha=0.8)
plt.title("Number of Iterations according to the Initial Guess")
plt.xlabel("Initial Guess (x0)")
plt.ylabel("Iterations")
plt.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
# Defining Function
import numpy as np

def f(x):
   return np.sin(4*x)*x

# Defining derivative of function
def g(x):
   return np.sin(4*x)+4*np.cos(4*x)*x

# Implementing Newton Method
def newton(x0,e,N):
   print('\n\n*** NEWTON METHOD IMPLEMENTATION ***')
   step = 1
   flag = 1
   condition = True
   while condition:
      if g(x0) == 0.0:
         print('Divide by zero error!')
         break
      x1 = x0 - f(x0)/g(x0)
      print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, x1, f(x1)))
      x0 = x1
      step = step + 1
      if step > N:
         flag = 0
         break
      condition = abs(f(x1)) > e
      if flag==1:
         print('\nRequired root is: %0.8f' % x1)
      else:
         print('\nNot Convergent.')
   return x1      
         
# Input Section
x0 = input('Enter Guess: ')
e = input('Tolerable Error: ')
N = input('Maximum Step: ')
# Converting x0 and e to float
x0 = float(x0)
e = float(e)
# Converting N to integer
N = int(N)
#Note: You can combine above three section like this
# x0 = float(input('Enter Guess: '))
# e = float(input('Tolerable Error: '))
# N = int(input('Maximum Step: '))
# Starting Newton Method
x1 = newton(x0,e,N)



#plot function

# Import pyplot as plt
import matplotlib.pyplot as plt


t = np.arange(min(x1,x0)-2, max(x1,x0)+2, 0.01)

#plot the function
ssin = f(t)
zero = [0] * len(t)
plt.plot(t, ssin, lw=2, label='function')
plt.plot(t, zero, lw=3)

# plot the root found
plt.plot(t, g(x0)*t-g(x0)*x0+f(x0), '-.', color='grey', label='differential', lw=1)
plt.plot(x1, f(x1), 'o', label='root')
plt.plot(x0, f(x0), 'o', label='starting guess')


plt.legend()
plt.show()
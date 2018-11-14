import sys
sys.path.append('/user/local/anaconda3/lib/python3.6/site-packages')

from numpy import *
x = linspace(0, 7)
y = sin(x)

from matplotlib import pyplot as plt
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Funkcija $cos(x)$')
plt.plot(x, y)
plt.show()

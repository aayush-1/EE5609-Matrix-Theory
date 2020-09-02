import numpy as np
import matplotlib.pyplot as plt


x1 = np.linspace(-10,10,100)
x2 = (12*np.ones(100) - 4*x1)/3

x3 = np.linspace(-10,10,100)
x4 = (32*np.ones(100) - 4*x1)/3

x5 = np.linspace(-10,10,100)
x6 = (-8*np.ones(100) - 4*x1)/3

x8 = np.zeros(100)
x7 = np.linspace(-10,10,100)

plt.plot(8,0,'o',label = "(8,0)")
plt.plot(-2,0,'o',label = "(-2,0)")
plt.plot(3,0,'o',label = "(3,0)")
plt.plot(x1,x2)
plt.plot(x3,x4)
plt.plot(x5,x6)
plt.plot(x7,x8)
plt.grid()
plt.legend()
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.show()
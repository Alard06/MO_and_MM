import numpy
import numpy as np
import matplotlib.pyplot as plt
import math

# V = ln(y + 0,95) + sin x^4

x = np.arange(0, 10.01, 1)
y = np.arange(0, 10.01, 1)
func = np.log(y+0.95) + np.sin(x**4)
plt.plot(func)
plt.grid()
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(('f (x)', ))
plt.show()

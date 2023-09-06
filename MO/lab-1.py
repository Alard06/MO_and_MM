# imports
import matplotlib.pyplot as plt
from scipy import optimize
import numpy as np

# practice
# a1=3, a2=2, a3=4; b1=4, b2=3, b3=1;
# c1=40, c2=28, c3=26;  A=3,  B=2.


def task1():
    matrix_a = np.array([[3, 4],
                         [2, 3],
                         [4, 1]
                         ])
    matrix_b = np.array([40, 28, 26])
    matrix_c = np.array([3, 2])
    res = optimize.linprog(-matrix_c, matrix_a, matrix_b)
    print(res)


def task2():
    x = np.linspace(0, 8, 60)
    y1 = (40-3*x)/4
    y2 = (28-2*x)/3
    y3 = 26-4*x

    plt.title('graf')
    plt.xlabel('x')
    plt.ylabel('y1,y2')
    plt.grid()
    plt.plot(x, y1, x, y2, x, y3)
    plt.show()

task1()
task2()
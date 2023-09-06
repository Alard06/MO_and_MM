# Решение систем линейных уравнений на Python
# imports
import numpy as np


# 3x + 2y + z = -8
# 2x + 3y + z = -3
# 2x + y + 3z = -1

coefficient = np.array([
    [3, 2, 1],
    [2, 3, 1],
    [2, 1, 3]
])

free_members = np.array([-8, -3, -1])


def test_infinity(matrix):
    if np.linalg.det(matrix) == 0:
        print('infinity')
        return 0
    else:
        return True


def task1():
    matrix_x = np.linalg.solve(coefficient, free_members)
    for x, t in zip(matrix_x, ['x1=', 'x2=','x3']):
        print(t, x)


def task2():
    test_infinity(coefficient)
    matrix = np.linalg.inv(coefficient)
    x = np.dot(matrix, free_members)
    print(x)


def task3():
    test_infinity(coefficient)
    s_0 = coefficient[:,0]
    s_1 = coefficient[:,1]
    s_2 = coefficient[:,2]

    coefficient_1 = np.column_stack((free_members,
                                     s_1,
                                     s_2)
                                    )
    coefficient_2 = np.column_stack((s_0, free_members, s_2))
    coefficient_3 = np.column_stack((s_0, s_1, free_members))

    x_1 = np.linalg.det(coefficient_1)/np.linalg.det(coefficient)
    x_2 = np.linalg.det(coefficient_2)/np.linalg.det(coefficient)
    x_3 = np.linalg.det(coefficient_3)/np.linalg.det(coefficient)

    print(f'x1 = {x_1}\nx2 = {x_2}\nx3 = {x_3}')


print('first method')
task1()
print('-' * 20)
print('second method')
task2()
print('-' * 20)
print('third method')
task3()
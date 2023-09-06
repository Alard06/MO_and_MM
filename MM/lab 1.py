# imports
import numpy as np

# ======== Задача 1 (стр. 30-31) / 22 ========

# Equation: G = (2A + B)T * (3C - 4D)


def task1():
    # matrix
    matrix_a = np.array([[2, -1], [3, 2], [5, -2]])
    matrix_b = np.array([[-2, -1], [11, -2], [5, 7]])
    matrix_c = np.array([[1, 3, 0, 4], [0, 2, -3, 5], [5, 3, 10, -2]])
    matrix_d = np.array([[-2, 5, 1, -3], [1, 1, -5, -4], [2, 6, 11, -1]])

    # Decision

    matrix_g = np.dot((matrix_a * 2 + matrix_b).transpose(), matrix_c * 3 - matrix_d * 4)

    print(matrix_g)

# ======== Задача 2 (стр. 32) / 30 ========!!!!!!!!!!!!!!!!!!!!

# Equation: f = x^3 + x^2 + x + 1


def task2():
    def equation(matrix):
        return np.linalg.matrix_power(matrix, 3) + np.linalg.matrix_power(matrix, 2) + matrix + 1

    # matrix
    matrix_a = np.array([[2, 0, 0], [0, 1, 0], [0, 0, 3]])

    print(equation(matrix_a))


# ======== Задача 3 (стр. 33) / 38 ========
def task3():
    matrix_c = np.array([[2, 4, 8, 0], [4, 8, 0, 27],
                         [8, 0, 27, 9], [0, 27, 9, 3]])
    print(f'Определитель матрицы: {np.linalg.det(matrix_c)}')


# ======== Задача 4 (стр. 34) / 47 ========
def task4():
    matrix_a = np.array([
        [-1, 0, 8, 6, -1, 5],
        [8, 4, -5, 4, -5, 11],
        [3, 6, -14, 7, 8, -2],
        [10, 4, 0, -4, -2, -6],
        [-6, -3, -4, -2, 2, 13],
        [-7, 8, 12, -4, 9, -5]
    ])
    print(np.linalg.inv(matrix_a))


if __name__ == '__main__':
    task1()
    task2()
    task3()
    task4()

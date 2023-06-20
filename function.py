from math import *
import numpy as np


def results(r, x1n, y1n, x2n, y2n):
    y = [
        [41, 45, 46, 49, 50, 54],
        [47, 52, 14, 17],
        [10, 13, 42, 48, 18, 22, 53, 51],
        [2, 15, 20],
        [11, 16, 19, 21],
        [1, 6, 12, 5, 9, 38, 43, 37, 44, 3, 25, 24, 23, 26, 57, 56, 58, 55, 0],
        [7, 33, 28, 29],
        [4, 34, 32],
        [39, 65, 36, 8, 27, 30, 60, 62],
        [66, 61, 35, 31],
        [68, 40, 67, 64, 63, 59]
    ]
    x = [
        [41, 45, 37, 44, 40, 68],
        [38, 43, 5, 9],
        [39, 65, 36, 8, 10, 13, 42, 48],
        [6, 12, 1],
        [11, 16, 7, 33],
        [46, 49, 47, 52, 14, 17, 15, 20, 2, 4, 34, 32, 31, 35, 61, 66, 67, 64, 0],
        [29, 28, 21, 19],
        [3, 25, 24],
        [62, 60, 30, 27, 22, 28, 53, 51, 18],
        [57, 56, 26, 23],
        [63, 59, 58, 55, 54, 50]
    ]

    res = []
    for i in range(69):
        res.append([f'''x{i},y{i}'''])

    for i in range(69):
        if i in x[0]:
            res[i].append(x1n)
        elif i in x[1]:
            res[i].append((x1n + x2n) / 2 - r)
        elif i in x[2]:
            res[i].append((x1n + x2n) / 2 - r * round(sqrt(2) / 2, 3))
        elif i in x[3]:
            res[i].append((x1n + x2n) / 2 - r / 2)
        elif i in x[4]:
            res[i].append((x1n + x2n) / 2 - r / 4)
        elif i in x[5]:
            res[i].append((x1n + x2n) / 2)
        elif i in x[6]:
            res[i].append((x1n + x2n) / 2 + r / 4)
        elif i in x[7]:
            res[i].append((x1n + x2n) / 2 + r / 2)
        elif i in x[8]:
            res[i].append((x1n + x2n) / 2 + r * round(sqrt(2) / 2, 3))
        elif i in x[9]:
            res[i].append((x1n + x2n) / 2 + r)
        elif i in x[10]:
            res[i].append(x2n)

        if i in y[0]:
            res[i].append(y1n)
        elif i in y[1]:
            res[i].append((y1n + y2n) / 2 - r)
        elif i in y[2]:
            res[i].append((y1n + y2n) / 2 - r * round(sqrt(2) / 2, 3))
        elif i in y[3]:
            res[i].append((y1n + y2n) / 2 - r / 2)
        elif i in y[4]:
            res[i].append((y1n + y2n) / 2 - r / 4)
        elif i in y[5]:
            res[i].append((y1n + y2n) / 2)
        elif i in y[6]:
            res[i].append((y1n + y2n) / 2 + r / 4)
        elif i in y[7]:
            res[i].append((y1n + y2n) / 2 + r / 2)
        elif i in y[8]:
            res[i].append((y1n + y2n) / 2 + r * round(sqrt(2) / 2, 3))
        elif i in y[9]:
            res[i].append((y1n + y2n) / 2 + r)
        elif i in y[10]:
            res[i].append(y2n)
    return res


def edge_index(uzel):
    edge = [
        [[0, 7], [7, 4], [4, 28], [28, 0]],
        [[0, 28], [28, 3], [3, 19], [19, 0]],
        [[0, 19], [19, 2], [2, 11], [11, 0]],
        [[0, 11], [11, 1], [1, 7], [7, 0]],
        [[5, 6], [6, 7], [7, 8], [8, 5]],
        [[9, 10], [10, 11], [11, 12], [12, 9]],
        [[13, 14], [14, 15], [15, 16], [16, 13]],
        [[17, 18], [18, 19], [19, 20], [20, 17]],
        [[21, 22], [22, 23], [23, 24], [24, 21]],
        [[25, 26], [26, 27], [27, 28], [28, 25]],
        [[29, 30], [30, 31], [31, 32], [32, 29]],
        [[33, 34], [34, 35], [35, 36], [36, 33]],
        [[37, 38], [38, 39], [39, 40], [40, 37]],
        [[41, 42], [42, 43], [43, 44], [44, 41]],
        [[45, 46], [46, 47], [47, 48], [48, 45]],
        [[49, 50], [50, 51], [51, 52], [52, 49]],
        [[53, 54], [54, 55], [55, 56], [56, 53]],
        [[57, 58], [58, 59], [59, 60], [60, 57]],
        [[61, 62], [62, 63], [63, 64], [64, 61]],
        [[65, 66], [66, 67], [67, 68], [68, 65]]
    ]

    kriv = [5, 9, 38, 43,
            8, 36, 39, 65,
            31, 35, 61, 66,
            27, 30, 60, 62,
            23, 26, 56, 57,
            18, 22, 51, 53,
            14, 17, 47, 52,
            10, 13, 42, 48]

    result = []
    for i in range(len(edge)):
        res = []
        for elem in edge[i]:
            r = []
            r.append(uzel[elem[0]])
            r.append(uzel[elem[1]])

            if elem[0] in kriv and elem[1] in kriv:
                r.append(((uzel[elem[0]][1] + uzel[elem[1]][1])/2, (uzel[elem[0]][2] + uzel[elem[1]][2])/2))
            else:
                r.append(0)

            res.append(r)
        result.append(res)
    return result


# Модуль Юнга диэлектрика
youngs_modulus = 5250

# Вычисление функций формы
def shape_functions(xi, eta):
    N = np.array([(1 - xi) * (1 - eta) / 4,
                  (1 + xi) * (1 - eta) / 4,
                  (1 + xi) * (1 + eta) / 4,
                  (1 - xi) * (1 + eta) / 4,
                  ((1 - xi**2) * (1 + eta) / 2)])
    return N

# Вычисление производных функций формы по локальным координатам
def shape_function_derivatives(xi, eta):
    dN_dxi = np.array([-(1 - eta) / 4,
                       (1 - eta) / 4,
                       (1 + eta) / 4,
                      -(1 + eta) / 4,
                      -xi * (1 + eta) / 2])

    dN_deta = np.array([-(1 - xi) / 4,
                       -(1 + xi) / 4,
                       (1 + xi) / 4,
                       (1 - xi) / 4,
                       (1 - xi**2) / 2])

    return dN_dxi, dN_deta

# Вычисление локальной матрицы жесткости



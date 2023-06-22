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


def shape_functions(x, y, xi, eta):

    dfdxi = -(1-eta)*x[0]/4 + (1-eta)*x[1]/4 + (1+eta)*x[2]/4 - (1+eta)*x[3]/4 - (1+eta)*x[4]

    dfdeta = -(1-xi)*x[0]/4 - (1+xi)*x[1]/4 + (1+xi)*x[2]/4 + (1-xi)*x[3]/4 - (1-xi*xi)*x[4]/2

    dfidxi = -(1-eta)*y[0]/4 + (1-eta)*y[1]/4 + (1+eta)*y[2]/4 - (1+eta)*y[3]/4 - (1+eta)*y[4]

    dfideta= -(1-xi)*y[0]/4 - (1+xi)*y[1]/4 + (1+xi)*y[2]/4 + (1-xi)*y[3]/4 - (1-xi*xi)*y[4]/2

    dn1dxi = -(1-eta)/4

    dn1deta = -(1-xi)/4

    dn2dxi = (1-eta)/4

    dn2deta = -(1+xi)/4

    dn3dxi = (1+eta)/4

    dn3deta = (1+xi)/4

    dn4dxi = -(1+eta)/4

    dn4deta = (1-xi)/4

    dn1dx = (dn1dxi * 1 / dfdxi) + (dn1deta * 1 / dfdeta)

    dn2dx = (dn2dxi * 1 / dfdxi) + (dn2deta * 1 / dfdeta)

    dn3dx = (dn3dxi * 1 / dfdxi) + (dn3deta * 1 / dfdeta)

    dn4dx = (dn4dxi * 1 / dfdxi) + (dn4deta * 1 / dfdeta)

    dn1dy = (dn1dxi * 1 / dfidxi) + (dn1deta * 1 / dfideta)

    dn2dy = (dn2dxi * 1 / dfidxi) + (dn2deta * 1 / dfideta)

    dn3dy = (dn3dxi * 1 / dfidxi) + (dn3deta * 1 / dfideta)

    dn4dy = (dn4dxi * 1 / dfidxi) + (dn4deta * 1 / dfideta)


    #Матрица B:
    B = [[dn1dx, 0, dn2dx, 0, dn3dx, 0, dn4dx, 0],
         [0, dn1dy, 0, dn2dy, 0, dn3dy, 0, dn4dy],
         [dn1dy, dn1dx, dn2dy, dn2dx, dn3dy, dn3dx, dn4dy, dn4dx]]

    # Матрица B транспонированная:
    Bt = [[dn1dx, 0, dn1dy],
          [0, dn1dy, dn1dx],
          [dn2dx, 0, dn2dy],
          [0, dn2dy, dn2dx],
          [dn3dx, 0, dn3dy],
          [0, dn3dy, dn3dx],
          [dn4dx, 0, dn4dy],
          [0, dn4dy, dn4dx]]

    # Якобиан:
    J = [[dfdxi, dfdeta],
         [dfidxi, dfideta]]

    J = abs(np.linalg.det(J))

    # Матрица L:
    L = [[-dn1dx, -dn2dx, -dn3dx, -dn4dx],
         [-dn1dy, -dn2dy, -dn3dy, -dn4dy]]


    # Матрица L транспонированная:
    Lt = [[-dn1dx, -dn1dy],
          [-dn2dx, -dn2dy],
          [-dn3dx, -dn3dy],
          [-dn4dx, -dn4dy]]

    res = [B, Bt, J, L, Lt]

    return res


def local_stiffness_matrix(x, y, flag):
    # Матрица C для пьезоэлектрика (Пьезокерамика ЦТС-19)
    C1 = [[11.22 * pow(10, 10), 6.22 * pow(10, 10), 0],
          [6.22 * pow(10, 10), 11.22 * pow(10, 10), 0],
          [0, 0, 2.49 * pow(10, 10)]]
    # Матрица e для Пьезоэлектрика (Пьезокерамика ЦТС-19)
    e = [[0, 0, 8.3878],
         [-6.127, 10.71, 0]]
    # Матрица Э для Пьезоэлектрика (Пьезокерамика ЦТС-19)
    E1 = [[7.257 * pow(10, -9), 0],
          [0, 8.274 * pow(10, -9)]]
    # Матрица C для упругого диэлектрика(Каучук)
    E = 0.008 * pow(10, 9)
    V = 0.47
    l = (E * V)/((1 + V) * (1 - 2 * V))
    m = E/(2 * (1 + V))

    C2 = [[l + 2 * m, l, 0],
          [l, l + 2 * m, 0],
          [0, 0, m]]
    # Матрица Э для для упругого диэлектрика(Каучук)
    e0 = 8.85 * pow(10, -12)
    e1 = 2.42 * e0
    E2 = [[e1, 0],
          [0, e1]]

    gauss_weights = [1, 1, 1, 1]
    gauss_coords = [[-1 / sqrt(3), -1 / sqrt(3)],
                    [-1 / sqrt(3), 1 / sqrt(3)],
                    [1 / sqrt(3), -1 / sqrt(3)],
                    [1 / sqrt(3), 1 / sqrt(3)]]

    Kuu = np.zeros((8, 8))
    Kufi = np.zeros((4, 8))
    Kfifi = np.zeros((4, 4))

    if flag:
        for i in range(len(gauss_weights)):
            xi, eta = gauss_coords[i]
            res = shape_functions(x, y, xi, eta)
            B = res[0]      # 8 x 3
            Bt = res[1]     # 3 x 8
            J = res[2]
            L = res[3]     # 4 x 2
            Lt = res[4]    # 2 x 4

            Kuu += np.dot(np.dot(Bt, C1), B) * J * gauss_weights[i]

            Kufi += np.dot(np.dot(Lt, e), B) * J * gauss_weights[i]

            Kfifi += np.dot(np.dot(Lt, E1), L) * J * gauss_weights[i]

    else:
        for i in range(len(gauss_weights)):
            xi, eta = gauss_coords[i]
            res = shape_functions(x, y, xi, eta)
            B = res[0]  # 8 x 3
            Bt = res[1]  # 3 x 8
            J = res[2]
            L = res[3]  # 4 x 2
            Lt = res[4]  # 2 x 4

            Kuu += np.dot(np.dot(Bt, C2), B) * J * gauss_weights[i]

            Kfifi += np.dot(np.dot(Lt, E2), L) * J * gauss_weights[i]

    local_matrix = np.block([[Kuu, Kufi.T],
                            [Kufi, Kfifi]])

    return local_matrix



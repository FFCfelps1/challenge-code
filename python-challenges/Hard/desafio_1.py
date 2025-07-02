#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matrixRotation' function below.
#
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY matrix
#  2. INTEGER r
#

def matrixRotation(matrix, r):
    m = len(matrix)
    n = len(matrix[0])
    layers = min(m, n) // 2

    result = [row[:] for row in matrix]  # copiar matriz original

    for layer in range(layers):
        elements = []

        # Coordenadas de limite da camada
        top, left = layer, layer
        bottom, right = m - layer - 1, n - layer - 1

        # Extrair a camada em ordem anti-horaria
        for i in range(left, right + 1):
            elements.append(matrix[top][i])
        for i in range(top + 1, bottom):
            elements.append(matrix[i][right])
        for i in range(right, left - 1, -1):
            elements.append(matrix[bottom][i])
        for i in range(bottom - 1, top, -1):
            elements.append(matrix[i][left])

        # Rotacionar a camada
        rot = r % len(elements)
        rotated = elements[rot:] + elements[:rot]

        # Recolocar a camada na matriz de resultado
        idx = 0
        for i in range(left, right + 1):
            result[top][i] = rotated[idx]
            idx += 1
        for i in range(top + 1, bottom):
            result[i][right] = rotated[idx]
            idx += 1
        for i in range(right, left - 1, -1):
            result[bottom][i] = rotated[idx]
            idx += 1
        for i in range(bottom - 1, top, -1):
            result[i][left] = rotated[idx]
            idx += 1

    # Imprimir a matriz resultante
    for row in result:
        print(" ".join(map(str, row)))


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    r = int(first_multiple_input[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)

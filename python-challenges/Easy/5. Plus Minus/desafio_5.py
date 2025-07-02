#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    size_array = len(arr)
    num_zeros = 0
    num_positivos = 0
    num_negativos = 0
    # Percorre o array e separa as categorias
    for i in range(len(arr)):
        if arr[i] > 0:
            num_positivos += 1
        elif arr[i] == 0:
            num_zeros += 1
        else:
            num_negativos += 1
    print(num_positivos/size_array)
    print(num_negativos/size_array)
    print(num_zeros/size_array)


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    arr.sort()
    soma = 0
    for numero in arr:
        soma += numero
    soma_max = soma - arr[0]
    soma_min = soma - arr[len(arr)-1]
    print(soma_min, soma_max)

        
    
    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

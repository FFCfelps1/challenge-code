#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Colocar em ordem crescente
    candles.sort()
    repeticoes = 0
    maior_valor = candles[len(candles)-1]
    
    for valor in candles:
        if valor == maior_valor:
            repeticoes +=1
    return repeticoes

if __name__ == '__main__':

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

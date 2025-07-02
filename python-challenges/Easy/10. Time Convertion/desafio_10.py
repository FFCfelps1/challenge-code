#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Extrai o sufixo AM ou PM
    periodo = s[-2:]
    
    # Remove o sufixo da string original
    s = s[:-2]
    
    # Separa em horas, minutos e segundos
    horas, minutos, segundos = s.split(":")

    if periodo == "AM":
        if horas == "12":
            horas = "00"
    else:  # PM
        if horas != "12":
            horas = str(int(horas) + 12)

    return f"{horas}:{minutos}:{segundos}"

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

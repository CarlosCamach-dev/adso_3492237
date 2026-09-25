#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    pointA = 0
    pointB = 0
    if len(a) >= len(b):
        for i in range(len(a)):
            if a[i] > b[i]:
                pointA += 1
            elif a[i] == b[i]:
                exit
            else:
                pointB += 1
    else:
        for i in range(len(b)):
            if a[i] > b[i]:
                pointA += 1
            elif a[i] == b[i]:
                exit
            else:
                pointB += 1
    return pointA, pointB
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

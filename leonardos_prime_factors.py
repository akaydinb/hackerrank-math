#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'primeCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def primeCount(n):
    if( n == 1 ): return 0;

    L = [ 2 ];
    P = [ ];

#https://stackoverflow.com/questions/11619942/print-series-of-prime-numbers-in-python
    for num in range(3, 54):
        prime = True
        for i in range(2, math.ceil(math.sqrt(num)) + 1):
            if(num % i == 0):
                prime = False
        
        if(prime):
            L.append(num * L[-1]);

    for i in range(1, len(L)):
        if( L[i] > n ):  return i;


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = primeCount(n)

        fptr.write(str(result) + '\n')

    fptr.close()

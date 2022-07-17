#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'divisors' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def divisors(n):
    # https://www.geeksforgeeks.org/print-all-prime-factors-of-a-given-number/
    print(n, "->");
    if(n % 2 != 0):
        return 0;
    
    primeFactors = { };

    while(n % 2 == 0):
        if 2 in primeFactors:
            primeFactors[2] = primeFactors[2] + 1;
        else:
            primeFactors[2] = 1;
        n = n // 2;

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while(n % i == 0):
            if i in primeFactors:
                primeFactors[i] = primeFactors[i] + 1;
            else:
                primeFactors[i] = 1;

            n = n // i;

    if(n > 2):
        primeFactors[n] = 1;

    c = 1;
    for key, value in primeFactors.items():
        if(key == 2):       c = c * value;
        else:               c = c * (value + 1);

    print(primeFactors);
    return c;

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = divisors(n)

        fptr.write(str(result) + '\n')

    fptr.close()

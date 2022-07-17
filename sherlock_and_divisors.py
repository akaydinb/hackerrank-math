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
    print("giren: ",n);
    if(n % 2 != 0):     return 0;

    count = 1;
    for i in range(2, int(math.sqrt(n)) + 1):
        if(i % 2 == 0):  # && ((n // i) % 2 == 0):
            count = count + 1;
        if((n // i) % 2 == 0):
            count = count + 1;
        if(n == i ** 2):
            count = count - 1;

    return count;

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = divisors(n)

        fptr.write(str(result) + '\n')

    fptr.close()

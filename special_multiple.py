#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER n as parameter.
#

def solve(n):
    c = 1;
    while(1):
        CC = int(format(c, "b")) * 9;
        if(CC % n == 0):
            return str(CC);
        c = c + 1;
        if(c > 10000):
            break;


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = solve(n)

        fptr.write(result + '\n')

    fptr.close()

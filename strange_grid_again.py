#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'strangeGrid' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER r
#  2. INTEGER c
#

def strangeGrid(r, c):
#    if(r % 2 == 0):     # r is even
#        return 2 * c - 1 + (r - 1) // 2 * 10;
#    else:               # r is odd
#        return 2 * c - 2 + (r - 1) // 2 * 10;    
    return 2 * c - 1 + (r - 1) // 2 * 10 - (r % 2);
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    result = strangeGrid(r, c)

    fptr.write(str(result) + '\n')

    fptr.close()

#!/usr/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'halloweenParty' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER k as parameter.
#

def halloweenParty(k):
    # Write your code here
    #b1 = k // 2;
    #b2 = -(k // -2);
    #return b1 * b2;
    return (k // 2) * -(k // -2);

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        k = int(input().strip())

        result = halloweenParty(k)

        fptr.write(str(result) + '\n')

    fptr.close()


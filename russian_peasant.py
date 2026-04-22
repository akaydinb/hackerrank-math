#!/usr/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#  3. LONG_INTEGER k
#  4. INTEGER m
#

def solve(a, b, k, m):
    # Write your code here
    T = tuple((a, b));
    P = tuple((0, 0));
    
    while((k % 2) == 0):
        tmp1 = (T[0] - T[1]) * (T[0] + T[1]);
        tmp2 = 2 * T[0] * T[1]
        T = (( tmp1 % m, tmp2 % m ));
        k = k // 2;

    P = T;
    k = k // 2;

    while(k > 0):
        tmp1 = (T[0] - T[1]) * (T[0] + T[1]);
        tmp2 = 2 * T[0] * T[1]
        T = (( tmp1 % m, tmp2 % m ));

        if(k % 2):
            tmp1 = P[0] * T[0] - P[1] * T[1];
            tmp2 = P[0] * T[1] + P[1] * T[0];
            P = (( tmp1 % m, tmp2 % m));
        k = k // 2;

    return list(P);

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        k = int(first_multiple_input[2])

        m = int(first_multiple_input[3])

        result = solve(a, b, k, m)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()


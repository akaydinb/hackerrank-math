#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. 2D_INTEGER_ARRAY queries
#

def solve(arr, queries):
    return_array = [ ];

    for query1 in queries:
        # States: 
        # 1- Normal state: Base even => even; Base odd => odd
        # 2- If query items are not equal (x != y) and next item is zero then Odd (n^0 = 1)
        # 3- If query items are equal the above check should never be run, because n^1 = n, 
        #    in case n is even but next number is zero, it returns Odd which is wrong. 
        if(arr[query1[0] - 1] & 1):
            return_array.append("Odd");
        elif((query1[0] != query1[1]) and arr[query1[0]] == 0):
            return_array.append("Odd");
        else:
            return_array.append("Even");
    return return_array;

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = solve(arr, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()

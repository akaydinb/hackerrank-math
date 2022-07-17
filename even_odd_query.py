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
        # 2^0'da base çift olmasina ragmen sonuc tek olmasi asagidaki OR kontrol ediliyor
        # ama yine de atladigim istisnai bir durum olmali.!
        if((arr[query1[0] - 1] % 2 != 0) or (arr[query1[0] - 1] == 2 and arr[query1[0]] == 0)):
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

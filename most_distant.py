#!/usr/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a DOUBLE.
# The function accepts 2D_INTEGER_ARRAY coordinates as parameter.
#

def solve(coordinates):
    # Write your code here
    Xmax = coordinates[0][0]; Xmin = coordinates[0][0];
    Ymax = coordinates[0][1]; Ymin = coordinates[0][1];

    for i in coordinates:
        if(Xmax < i[0]):
            Xmax = i[0]
        if(Xmin > i[0]):
            Xmin = i[0]
        if(Ymax < i[1]):
            Ymax = i[1]
        if(Ymin > i[1]):
            Ymin = i[1]

    Xabs = Xmax - Xmin
    Yabs = Ymax - Ymin

    Xmax = coordinates[0][0]; Xmin = coordinates[0][0];
    Ymax = coordinates[0][1]; Ymin = coordinates[0][1];

    for i in coordinates:
        if(Xmax < i[0]):
            Xmax = i[0]
        if(Xmin > i[0]):
            Xmin = i[0]
        if(Ymax < i[1]):
            Ymax = i[1]
        if(Ymin > i[1]):
            Ymin = i[1]

    Xabs = Xmax - Xmin
    Yabs = Ymax - Ymin

    return max(Xabs, Yabs)
    Xmax = coordinates[0][0]; Xmin = coordinates[0][0];
    Ymax = coordinates[0][1]; Ymin = coordinates[0][1];

    for i in coordinates:
        if(Xmax < i[0]):
            Xmax = i[0]
        if(Xmin > i[0]):
            Xmin = i[0]
        if(Ymax < i[1]):
            Ymax = i[1]
        if(Ymin > i[1]):
            Ymin = i[1]

    Xabs = Xmax - Xmin
    Yabs = Ymax - Ymin

    # For Example given points (0,0) (1,0) (0,1)
    # Considering the distances along the axes only
    # won't give the correct result.
    XY1 = math.sqrt(Xmax * Xmax + Ymax * Ymax)
    XY2 = math.sqrt(Xmax * Xmax + Ymin * Ymin)
    XY3 = math.sqrt(Xmin * Xmin + Ymax * Ymax)
    XY4 = math.sqrt(Xmin * Xmin + Ymin * Ymin)

    return(max( [ Xabs, Yabs, XY1, XY2, XY3, XY4 ] ))

        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    coordinates = []

    for _ in range(n):
        coordinates.append(list(map(int, input().rstrip().split())))

    result = solve(coordinates)

    fptr.write(str(result) + '\n')

    fptr.close()


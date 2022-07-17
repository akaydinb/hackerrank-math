#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    t = int(input().strip())

    for _ in range(1, t + 1):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        if(k < (n // 2)):
            print(2 * k + 1);
        else:
            print(2 * (n - k - 1));

#!/bin/python3

import math
import os
import random
import re
import sys

def calcsd(x):
    sd = x % 10;
    while(x > 0):
        x = x // 10;
        sd = sd + x % 10;

    return sd;

if __name__ == '__main__':
    n = int(input().strip())

    factors = set([1, n]);
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if( n % i == 0 ):
            factors.add(i);
            factors.add(n // i);

    IMax = 0; SDMax = 0;
    for i in list(factors):
        if(SDMax < calcsd(i)):
            SDMax = calcsd(i);
            IMax = i;
        elif(SDMax == calcsd(i)):
            if(IMax > i):
                IMax = i;
    
    print(IMax);
        

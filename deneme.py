#!/bin/python3

import math;

if __name__ == '__main__':
    n = 2;
    m = 3;
    
    print(math.comb(m + n - 2, n - 1));

SAW
LEFT
RIGHT


3=> [1,3], [2,2], [3,1]
      1      2      1
    (2,0)  (2,1)  (2,2)

4=> [1,4], [2,3], [3,2], [4,1]
      1      3      3      1
    (3,0)  (3,1)  (3,2)  (3,3)

5=> [1,5], [2,4], [3,3], [4,2], [5,1]
      1      4      6      4      1
    (4,0)  (4,1)  (4,2)  (4,3)  (4,4)


((m+n-1),(m-1))

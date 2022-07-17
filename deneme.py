#!/bin/python3

import os

A = [ 3, 2, 0, 7 ];

def find(x, y):
    if(x > y):
        return 1
    ans = pow(A[x - 1], find(x + 1, y));
    return ans

def solve(arr, queries):
    return_array = [ ];

    for query1 in queries:
        if((arr[query1[0] - 1] % 2 != 0) or (arr[query1[0] - 1] == 2 and arr[query1[0]] == 0)):
            return_array.append("Odd");
        else:
            return_array.append("Even");
    
    return return_array;

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    print(find(1, 3));
    print(find(2, 3));
    print(find(1, 4));
    print(find(2, 4));

    result = solve(A, [[1,3], [2,3], [1,4], [2,4]]);
    
    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
    

# x = 1, y = 3
# pow(3, 128)
# x = 2, y = 3
# pow(2, 7)
# x = 3, y = 3
# pow(7, 1)

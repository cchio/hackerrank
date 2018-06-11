#!/bin/python3

import math
import os
import random
import re
import sys

ip = """1
12 3
2 3 4"""

# Complete the stoneDivision function below.
def stoneDivision(n, s):
    

if __name__ == '__main__':
    if len(sys.argv) > 1:
        
    else:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
        q = int(input())
        for q_itr in range(q):
            nm = input().split()
            n = int(nm[0])
            m = int(nm[1])
            s = list(map(int, input().rstrip().split()))
            result = stoneDivision(n, s)
            fptr.write(str(result) + '\n')
        fptr.close()

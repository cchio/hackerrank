#!/usr/local/bin/python3

import math
import os
import random
import re
import sys

sqr = None

def calc(x, n, cur):
    if x == 0:
        return 1
    if x < 0 or cur > sqr:
        return 0
    return calc(x, n, cur+1) + calc(x-(cur**n), n, cur+1)

def powerSum(x, n):
    return calc(x, n, 1)
    
if __name__ == '__main__':
    X = 100
    N = 2
    sqr = math.floor(X**(1./N))
    result = powerSum(X, N)
    print(result)

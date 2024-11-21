#!/bin/python3

import math
import os
import random
import re
import sys

def pageCount(n, p):
    
    forward = p // 2
    backward = (n-p+1)//2 if n % 2 == 0 else (n-p)//2
    return min(forward, backward)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()

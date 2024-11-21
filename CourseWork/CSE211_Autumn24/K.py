
import math
import os
import random
import re
import sys

def migratoryBirds(arr):
    birds =[0] * len(arr)
    
    for i in range(len(arr)):
        birds[arr[i]] += 1
        
    return birds.index(max(birds))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

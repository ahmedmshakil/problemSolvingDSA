import math
import os
import random
import re
import sys

def birthdayCakeCandles(candles):
    count = 0
    
    tallest = max(candles)
    for i in range(len(candles)):
        if(candles[i]== tallest):
            count = count + 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
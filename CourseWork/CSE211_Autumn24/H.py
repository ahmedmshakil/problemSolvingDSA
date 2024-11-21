import math
import os
import random
import re
import sys


def timeConversion(s):
    h, m, sec = s[:-2].split(':')
    if s[-2:] == "AM":
        h = "00" if h == "12" else h 
    else:
        h = str(int(h) % 12 + 12)
    return f"{h}:{m}:{sec}"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

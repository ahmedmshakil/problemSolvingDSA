#!/bin/python3

import math
import os
import random
import re
import sys



def miniMaxSum(arr):
    # Write your code here
    total_sum = sum(arr)
    
    min_sum = total_sum - max(arr)
    max_sum = total_sum - min(arr)
    
    print(min_sum, max_sum)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

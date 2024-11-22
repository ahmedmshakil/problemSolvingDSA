import os
import sys

def getMoneySpent(keyboards, drives, b):
    
    max_budget = 0
    cost_list  = []
    
    for i in keyboards:
        for j in drives:
            max_budget = i + j
            if max_budget <= b:
                cost_list.append(max_budget)
            else:   
                cost_list.append(-1)
    return max(cost_list)
    
    
    
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()

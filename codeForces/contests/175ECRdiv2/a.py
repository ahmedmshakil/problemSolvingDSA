# shakil_13_175ECRdiv2_a.py
def count_fizzbuzz(n):
    q = n // 15  
    r = n % 15  
    return 3 * q + min(r + 1, 3) 

t = int(input())
for _ in range(t):
    n = int(input())
    print(count_fizzbuzz(n))
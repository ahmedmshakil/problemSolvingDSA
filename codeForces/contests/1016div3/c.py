# shakil_13_1016iv3_c.py
# k is an ideal generator if and only if k is odd.
# t = int(input().strip())
def is_prime(n):
    
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True
t = int(input())
for _ in range(t):
    x, k = map(int, input().split())
    if k == 1:
        if is_prime(x):
            print("YES")
        else:
            print("NO")
    elif k == 2 and x == 1:
        print("YES")
    else:
        print("NO")
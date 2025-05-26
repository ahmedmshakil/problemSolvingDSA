# shakil_13_1027div3_a.py

import math
t = int(input())
for _ in range(t):
    s = input().strip()
    n = int(s)
    k = int(math.sqrt(n))
    if k * k == n:
        print(0, k)
    else:
        print(-1)
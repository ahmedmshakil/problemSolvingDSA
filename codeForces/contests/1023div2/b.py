# shakil_13_1023div2_b.py
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    mx = max(a)
    mn = min(a)
    d = mx - mn
    if d > k+1 or (d == k+1 and a.count(mx) > 1):
        print("Jerry")
    else:
        t = sum(a)
        print("Tom" if t & 1 else "Jerry")

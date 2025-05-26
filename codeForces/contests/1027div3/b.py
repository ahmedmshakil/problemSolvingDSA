# shakil_13_1027div3_b.py
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()
    
    c1 = s.count('0')
    c2 = n - c1
    half = n // 2
    c = half - k
    if c < 0 or c > c1 or c > c2:
        print("NO")
        continue
    if (c1 - c) % 2 == 0:
        print("YES")
    else:
        print("NO")

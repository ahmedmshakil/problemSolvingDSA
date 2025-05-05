# shakil_13_1023div2_a.py
import sys
import math

def solve():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        p = [0] * (n + 1)
        for i in range(n):
            p[i + 1] = math.gcd(p[i], a[i])
        s = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            s[i] = math.gcd(s[i + 1], a[i])
        c = -1
        for i in range(n):
            if math.gcd(p[i], s[i + 1]) != a[i]:
                c = i
                break
        if c == -1:
            print("No")
        else:
            print("Yes")
            ans = ['2'] * n
            ans[c] = '1'
            print(" ".join(ans))

if __name__ == "__main__":
    solve()

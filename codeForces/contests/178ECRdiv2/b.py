# shakil_13_178ECRdiv2_b.py
import sys
input = sys.stdin.readline

def skl():
    t = int(input())
    o = []
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        M = [0] * n
        M[0] = a[0]
        for i in range(1, n):
            M[i] = max(M[i-1], a[i])
        s = [0] * (n+1)
        for i in range(n-1, -1, -1):
            s[i] = a[i] + s[i+1]
        a = [0] * n
        for k in range(1, n+1):
            idx = n - k
            a[k-1] = M[idx] + s[idx+1]
        o.append(" ".join(str(x) for x in a))
    print("\n".join(o))

if __name__ == "__main__":
    skl()

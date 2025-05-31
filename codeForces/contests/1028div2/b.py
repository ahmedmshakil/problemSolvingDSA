# shakil_13_1028div2_b_fast.py
# Note :>>
# Time limit exceeded on pretest 3 -cf judge 
# most disaster round, I have ever faced in codeforces, cant even solve a single problem in div 2


import sys
input = sys.stdin.readline
MOD = 998244353 #9bit mod value

def solve():
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    a = [pow(2, x, MOD) for x in p]
    b = [pow(2, x, MOD) for x in q]
    r = [0] * n
    for i in range(n):
        ms = 0
        for j in range(i + 1):
            t = a[j] + b[i - j]
            if t >= MOD:
                t -= MOD
            if t > ms:
                ms = t
        r[i] = ms
    print(" ".join(map(str, r)))
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()

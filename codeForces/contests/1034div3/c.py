#shakil_13_1034div3_c.py

# pm-sm >>array [i] = 1 if a[i] ispm to i

import sys
input = sys.stdin.readline

def skl():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        pm = [0]*n
        pm[0] = a[0]
        for i in range(1, n):
            pm[i] = min(pm[i-1], a[i])
            
        sm = [0]*n
        sm[-1] = a[-1]
        for i in range(n-2, -1, -1):
            sm[i] = max(sm[i+1], a[i])
        ans = ['0']*n
        for i in range(n):
            if a[i] == pm[i] or a[i] == sm[i]:
                ans[i] = '1'

        print(''.join(ans))

if __name__ == "__main__":
    skl()

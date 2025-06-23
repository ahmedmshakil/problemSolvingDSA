#shakil_13_ECR_180_div2_b.py

import sys

def skl():
    data = sys.stdin.read().split()
    t = int(data[0])
    p = []
    idx = 1
    for _ in range(t):
        n = int(data[idx]); idx+=1
        a = list(map(int, data[idx:idx+n])); 
        idx= idx + n
        f0 = False
        for i in range(n-1):
            if abs(a[i] - a[i+1]) <= 1:
                f0 = True
                break
        if f0:
            p.append('0')
            continue
        if n == 2:
            p.append('-1')
            continue
        
        f1 = False
        for i in range(n-1):
            lo, hi = min(a[i], a[i+1]), max(a[i], a[i+1])
            if i-1 >= 0:
                if max(lo, a[i-1]-1) <= min(hi, a[i-1]+1):
                    f1 = True
                    break
            if i+2 < n:
                if max(lo, a[i+2]-1) <= min(hi, a[i+2]+1):
                    f1 = True
                    break
        p.append('1' if f1 else '-1')
    sys.stdout.write("\n".join(p))

if __name__ == '__main__':
    skl()

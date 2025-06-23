#shakil_13_ECR_180_div2_a.py

import sys

def skl():
    data = sys.stdin.read().split()
    t = int(data[0])
    ans = []
    idx = 1
    for _ in range(t):
        a = int(data[idx]); x = int(data[idx+1]); y = int(data[idx+2])
        idx += 3
        found = False
        for b in range(1, 101):
            if b == a:
                continue
            if abs(b - x) < abs(a - x) and abs(b - y) < abs(a - y):
                found = True
                break
        ans.append("YES" if found else "NO")
    sys.stdout.write("\n".join(ans))

if __name__ == '__main__':
    skl()

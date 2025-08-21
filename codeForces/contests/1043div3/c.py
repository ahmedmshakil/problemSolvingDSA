#shakil_13_1043div3_c.py (Easy Version)
import sys

def skl():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    ns = data[1:]
    P = [1]
    
    for _ in range(1, 21):
        P.append(P[-1]*3)
    c = [0]*len(P)
    for x in range(len(P)-1):
        if x == 0:
            c[x] = P[1]
        else:
            c[x] = P[x+1] + x * P[x-1]
    o = []
    for n in ns:
        ans = 0
        i = 0
        while n:
            d = n % 3
            if d:
                ans += d * c[i]
            n //= 3
            i += 1
        o.append(str(ans))
    sys.stdout.write("\n".join(o))

if __name__ == "__main__":
   skl()

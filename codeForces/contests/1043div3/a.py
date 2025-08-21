#shakil_13_1043div3_a.py
import sys
from collections import deque


def skl():
    data = sys.stdin.read().split()
    it = iter(data)
    t = int(next(it))
    ol = []
    for _ in range(t):
        n = int(next(it))
        a = next(it)
        m = int(next(it))
        b = next(it)
        c = next(it)
        dq = deque(a)
        
        for i in range(m):
            if c[i] == 'V':
                dq.appendleft(b[i])
            else:
                dq.append(b[i])
        ol.append(''.join(dq))
    sys.stdout.write('\n'.join(ol))

if __name__ == "__main__":
    skl()

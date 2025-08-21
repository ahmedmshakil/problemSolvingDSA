#shakil_13_1043div3_b.py
import sys

def skl():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    ol = []
    x = 1
    for _ in range(t):
        n = int(data[x]); x += 1
        ans = []
        p = 10
        while p + 1 <= n:
            d = p + 1
            if n % d == 0:
                ans.append(n // d)
            p *= 10
        if not ans:
            ol.append("0")
        else:
            ans.sort()
            ol.append(str(len(ans)))
            ol.append(" ".join(map(str, ans)))
    sys.stdout.write("\n".join(ol))

if __name__ == "__main__":
    skl()


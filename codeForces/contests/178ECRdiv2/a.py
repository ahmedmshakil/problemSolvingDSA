# shakil_13_178ECRdiv2_a.py
import sys
input = sys.stdin.readline

def eq(a, b, c):
    t = a + b + c
    if t % 3 != 0:
        return False
    T = t // 3
    return T >= b

def skl():
    t = int(input())
    o = []
    for _ in range(t):
        a, b, c = map(int, input().split())
        o.append("YES" if eq(a, b, c) else "NO")
    print("\n".join(o))

if __name__ == "__main__":
    skl()

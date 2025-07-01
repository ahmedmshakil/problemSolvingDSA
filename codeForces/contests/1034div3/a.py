#shakil_13_1034div3_a.py
import sys

def skl():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n = int(input())
        b = n // 4
        rem  = n % 4
        c = [b + (1 if r < rem else 0) for r in range(4)]
        K = min(c[0], c[3]) + min(c[1], c[2])
        print("Bob" if 2*K == n else "Alice")

if __name__ == "__main__":
    skl()

#shakil_13_1034div3_b.py
import sys

def skl():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n, j, k = map(int, input().split())
        a = list(map(int, input().split()))
        aj = a[j-1]
        m = sum(1 for x in a if x > aj)

        if k == 1:
            print("YES" if m == 0 else "NO")
        else:
            print("YES") # for K>=2 -tc 2
            
if __name__ == "__main__":
    skl()

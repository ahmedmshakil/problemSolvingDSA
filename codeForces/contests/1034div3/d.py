#shakil_13_1034div3_d.py
import sys


def skl():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        s = input().strip()
        cnt = s.count('1')
        if cnt <= k:
            print("Alice")
            continue
        l = [0]*n
        r = [0]*n
        l[0] = 1
        for i in range(1, n):
            if s[i] == s[i-1]:
                l[i] = l[i-1] + 1
            else:
                l[i] = 1
        r[-1] = 1
        for i in range(n-2, -1, -1):
            if s[i] == s[i+1]:
                r[i] = r[i+1] + 1
            else:
                r[i] = 1
        bs = True
        for i in range(n - k + 1):
            if l[i+k-1] < k and r[i] < k:
                bs = False
                break

        print("Bob" if bs else "Alice")

if __name__ == "__main__":
    skl()

# Wrong answer on test 1
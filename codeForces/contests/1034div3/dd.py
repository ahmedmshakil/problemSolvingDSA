#shakil_13_1034div3_d.py

import sys

def skl():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        s = input().strip()
        t = s.count('1')
        if t <= k:
            print("Alice")
            continue
        w = sum(1 for c in s[:k] if c == '1')
        x = True
        curr = w
        for i in range(k, n):
            if s[i] == '1':
                curr += 1
            if s[i-k] == '1':
                curr -= 1
            if curr != w:
                x = False
                break

        if x:
            print("Bob")
        else:
            print("Alice")

if __name__ == "__main__":
    skl()


# Wrong answer on test 1
# 1009div3_by Shakil

import sys

def is_power_of_two(n):
    return (n & (n - 1)) == 0

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        x = int(sys.stdin.readline())
        if is_power_of_two(x) or (x & (x + 1)) == 0:
            print(-1)
        elif x % 2 == 0:
            print(x - 1)
        else:
            h = 1 << (x.bit_length() - 1)
            print(h - 1)

if __name__ == '__main__':
    solve()
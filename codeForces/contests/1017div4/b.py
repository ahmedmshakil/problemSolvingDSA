# shakil_13_1017div3_a.py
#
# >> m moves -- dis -- in the same ratio as left moves to total moves


def solve():
    import sys
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n, m, l, r = map(int, input().split())
        total_left = -l 
        x = round(m * total_left / n) 
        y = m - x                    
        l_prime = -x
        r_prime = y
        print(l_prime, r_prime)

if __name__ == '__main__':
    solve()


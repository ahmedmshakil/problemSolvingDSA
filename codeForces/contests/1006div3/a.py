def solve(n, k, p):
    if k == 0:
        return 0
    m = (abs(k) + p - 1) // p
    return m if m <= n else -1
t = int(input())
for _ in range(t):
    n, k, p = map(int, input().split())
    print(solve(n, k, p))
t = int(input())
for _ in range(t):
    n, m, r, c = map(int, input().split())
    i = (r - 1) * m + c
    ans = (n - r + 1) * m - c + (m - 1) * (n - r)
    print(ans)
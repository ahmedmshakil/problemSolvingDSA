def solve():
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        grid = [[0] * m for _ in range(n)]
        counter = 0
        for i in range(n):
            if i % 2 == 0:
                for j in range(m):
                    grid[i][j] = (counter % k) + 1
                    counter += 1
            else:
                for j in range(m - 1, -1, -1):
                    grid[i][j] = (counter % k) + 1
                    counter += 1
        for row in grid:
            print(' '.join(map(str, row)))

if __name__ == "__main__":
    solve()
t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    a, b = map(int, input().split())
    x, y = min(x, y), max(x, y)
    cost = min((x + y) * a, x * b + (y - x) * a)

    print(cost)

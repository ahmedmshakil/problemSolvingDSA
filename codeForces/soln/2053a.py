t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    found = False
    for i in range(n - 1):
        min_val = min(a[i], a[i+1])
        max_val = max(a[i], a[i+1])
        if 2 * min_val > max_val:
            print("YES")
            found = True
            break
    if not found:
        print("NO")
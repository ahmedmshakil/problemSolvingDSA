# shakil_13_1020div3_b.py
t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    if x == 0:
        p = list(range(1, n)) + [0]
    else:
        p = list(range(x)) 
        r = list(range(x + 1, n))
        p += r
        if x < n:
            p.append(x) 
    print(' '.join(map(str, p)))

# shakil_13_177ECRdiv2_c.py

t = int(input())
for _ in range(t):
    n = int(input())
    p = [0] + list(map(int, input().split()))
    d = [0] + list(map(int, input().split()))
    pos = [0] * (n + 1)
    for i in range(1, n + 1):
        pos[d[i]] = i
    
    v = [False] * (n + 1)
    add = [0] * (n + 1) 
    for m in range(1, n + 1):
        if not v[m]:
            cycle = []
            k = m
            while not v[k]:
                v[k] = True
                cycle.append(k)
                k = p[k]
            min_pos = min(pos[k] for k in cycle)
            size = len(cycle)
            add[min_pos] += size
    
    current_S = 0
    for i in range(1, n + 1):
        current_S += add[i]
        print(current_S, end=' ')
    print()  
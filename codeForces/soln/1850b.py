t = int(input())

for _ in range(t):
    n = int(input())
    max_quality = -1
    winner = -1

    for i in range(1, n + 1):
        ai, bi = map(int, input().split())
        
        if ai <= 10:
            if bi > max_quality:
                max_quality = bi
                winner = i
    print(winner)

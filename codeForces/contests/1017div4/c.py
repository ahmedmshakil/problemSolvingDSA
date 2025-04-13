# shakil_13_1017div3_c.py
# 
# 
# output:
# 5 1 6 2 4 3 
# 2 1 
# 1 2 3 4 

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        G = [list(map(int, input().split())) for _ in range(n)]
        gn = set()
        
        for row in G:
            for num in row:
                gn.add(num)
        fs = set(range(1, 2*n + 1))
        p1 = (fs - gn).pop()
        p = [0] * (2*n + 1)
        p[1] = p1
        
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                k = i + j
                p[k] = G[i - 1][j - 1] 
        print(' '.join(map(str, p[1:2*n + 1])))
        
if __name__ == '__main__':
    solve()
    



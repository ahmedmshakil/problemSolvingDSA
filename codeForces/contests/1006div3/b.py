# shakil_13_1006div3_b.py
def solve():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    t = int(data[0])
    res = []
    index = 1
    for _ in range(t):
        n = int(data[index])
        index += 1
        s = data[index]
        index += 1
        
        dash = s.count('-')
        underscore = s.count('_')
        if dash < 2 or underscore < 1:
            res.append("0")
            continue
        
        left = dash // 2
        right = (dash + 1) // 2
        ans = underscore * left * right
        res.append(str(ans))
        
    sys.stdout.write("\n".join(res))
    
if __name__ == '__main__':
    solve()

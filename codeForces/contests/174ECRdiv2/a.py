# Shakil_174ECR

def solve():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    out_lines = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        b = list(map(int, data[idx: idx + n - 2]))
        idx += n - 2
        dp_prev = {0, 1}  
        possible = True
        for i in range(2, n):
            cur_b = b[i - 2]
            dp_curr = set()
            for prev in dp_prev:
                for cur in (0, 1):
                    if cur_b == 1:
                        if prev == 1 and cur == 1:
                            dp_curr.add(cur)
                    else:
                        if not (prev == 1 and cur == 1):
                            dp_curr.add(cur)
            dp_prev = dp_curr
            if not dp_prev:
                possible = False
                break
        
        out_lines.append("YES" if possible and dp_prev else "NO")
    sys.stdout.write("\n".join(out_lines))
    
if __name__ == '__main__':
    solve()

# shakil_13_1013div3_c.py
def solve():
    import sys
    data = sys.stdin.read().strip().split()
    if not data: 
        return
    t = int(data[0])
    results = []
    idx = 1
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        if n % 2 == 0:
            results.append("-1")
        else:
            perm = []
            for i in range(1, n+1):
                val = (2 * i) % n
                if val == 0:
                    val = n
                perm.append(str(val))
            results.append(" ".join(perm))
    sys.stdout.write("\n".join(results))
    
if __name__ == '__main__':
    solve()

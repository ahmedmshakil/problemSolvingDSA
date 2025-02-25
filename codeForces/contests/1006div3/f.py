# shakil_13_1006div3_problemF
def solve():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    output_lines = []
    idx = 1
    for _ in range(t):
        n = int(data[idx]); idx += 1
        k = int(data[idx]); idx += 1
        m = n - 1  
        row = []
        for j in range(n): 
            if (j | m) == m:
                row.append(str(k))
            else:
                row.append("0")
        output_lines.append(" ".join(row))
    sys.stdout.write("\n".join(output_lines))

if __name__ == '__main__':
    solve()

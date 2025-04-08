# shakil_13_1016iv3_b.py

def solve():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    # input = sys.stdin.read
    # data = input().split()

    t = int(data[0])
    results = []
    p = 1
    for _ in range(t):
        s = data[p]
        p += 1
        n = len(s)
        mk = 0
        zc = 0
        for ch in s:
            if ch == '0':
                zc += 1
            else:
                candidate = zc + 1
                if candidate > mk:
                    mk = candidate
        results.append(str(n - mk))
    sys.stdout.write("\n".join(results))

if __name__ == '__main__':
    solve()

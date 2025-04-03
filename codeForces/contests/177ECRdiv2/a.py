# shakil_13_177ECRdiv2_a.py
def solve():
    import sys
    input_data = sys.stdin.read().split()
    t = int(input_data[0])
    results = []
    # logic
    for i in range(1, t + 1):
        n = int(input_data[i])
        results.append(str(2 * n))
    sys.stdout.write("\n".join(results))

if __name__ == "__main__":
    solve()

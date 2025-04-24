# shakil_13_1020div3_a.py
def skl():
    import sys
    data = sys.stdin.read().split()
    t = int(data[0])
    
    idx = 1
    for _ in range(t):
        n = int(data[idx]); idx += 1
        s = data[idx]; idx += 1
        op = s.count('1')
        print((n - 2) * op + n)

if __name__ == "__main__":
    skl()

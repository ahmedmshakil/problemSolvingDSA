# shakil_13_1020div3_c.py

def skl():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        val = set()
        elm = False
        
        for i in range(n):
            if b[i] != -1:
                elm = True
                val.add(a[i] + b[i])
        if len(val) > 1:
            print(0)
            continue
        if not elm:
            mn = max(a)
            mx = min([a[i] + k for i in range(n)])
            if mn <= mx:
                print(mx - mn + 1)
            else:
                print(0)
        else:
            x = next(iter(val))
            res = True
            for i in range(n):
                if b[i] == -1:
                    bi = x - a[i]
                    if bi < 0 or bi > k:
                        res = False
                        break
            
            print(1 if res else 0)

if __name__ == "__main__":
    skl()

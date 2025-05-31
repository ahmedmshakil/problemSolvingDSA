# shakil_13_1028div2_a.py
# Note :>>
# Wrong answer on pretest 2 -cf judge 
# most disaster round, I have ever faced in codeforces, cant even solve a single problem in div 2


import sys
input = sys.stdin.readline
 
def solve():
    t = int(input().strip())
    r = []
    for _ in range(t):
        a, b, c, d = map(int, input().split())
        
        if a == 0:
            r.append("Flower")
        elif b == 0:
            r.append("Gellyfish")
        elif b == 1:
            r.append("Gellyfish")
        else:
            if d >= b:
                r.append("Flower")
            elif c >= a:
                r.append("Gellyfish")
            elif a > d:
                r.append("Gellyfish")
            elif b > c:
                r.append("Flower")
            else:
                r.append("Gellyfish")

    for res in r:
        print(res)
    
if __name__ == "__main__":
    solve()
    
    

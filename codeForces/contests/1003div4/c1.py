# shakil_13_codeforces1003_div4
def solve():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        n = int(data[index])
        m = int(data[index+1]) 
        index += 2
        
        a = list(map(int, data[index:index+n]))
        index += n
        
        b_val = int(data[index])
        index += m
        
        dp0 = True
        dp1 = True
        prev0 = a[0]
        prev1 = b_val - a[0]
        
        possible = True
        for i in range(1, n):
            cur0 = a[i]
            cur1 = b_val - a[i]
            new_dp0 = False
            new_dp1 = False
            # dp condition
            if dp0 and (prev0 <= cur0):
                new_dp0 = True
            if dp1 and (prev1 <= cur0):
                new_dp0 = True
            if dp0 and (prev0 <= cur1):
                new_dp1 = True
            if dp1 and (prev1 <= cur1):
                new_dp1 = True
            
            dp0, dp1 = new_dp0, new_dp1
            prev0 = cur0
            prev1 = cur1
            
            if not (dp0 or dp1):
                possible = False
                break
        
        results.append("YES" if possible and (dp0 or dp1) else "NO")
    sys.stdout.write("\n".join(results))

if __name__ == '__main__':
    solve()

# shakil_13_177ECRdiv2_b.py
# 
# initial logic >>
# R = remaining sum in the current copy if starting at position i

def solve():
    import sys
    input_data = sys.stdin.read().split()
    t = int(input_data[0])
    index = 1
    results = []
    
    for _ in range(t):
        n = int(input_data[index])
        k = int(input_data[index+1])
        x = int(input_data[index+2])
        index += 3
        a = list(map(int, input_data[index:index+n]))
        index += n
        S = sum(a)
        total_valid = 0
        prefix = 0
        
        # logic
        for i in range(n):
            R = S - prefix
            if R >= x:
                total_valid += k
            else:
                need = x - R
                m = (need + S - 1) // S  
                if m < k:
                    total_valid += (k - m)
            prefix += a[i]
            
            
            
        results.append(str(total_valid))
    sys.stdout.write("\n".join(results))

if __name__ == "__main__":
    solve()

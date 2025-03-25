# shakil_13_1013div3_b.py
def solve():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    
    t = int(data[0])
    index = 1
    req = {0: 3, 1: 1, 2: 2, 3: 1, 5: 1}
    
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        digits = list(map(int, data[index:index+n]))
        index += n
        
        freq = {}
        answer = 0
        
        for i, d in enumerate(digits, start=1):
            freq[d] = freq.get(d, 0) + 1
            if (freq.get(0, 0) >= req[0] and
                freq.get(1, 0) >= req[1] and
                freq.get(2, 0) >= req[2] and
                freq.get(3, 0) >= req[3] and
                freq.get(5, 0) >= req[5]):
                answer = i
                break
        
        results.append(str(answer))
    
    sys.stdout.write("\n".join(results))

if __name__ == '__main__':
    solve()

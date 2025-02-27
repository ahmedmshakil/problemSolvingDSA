# shakil_13_175ECRdiv2_b.py
def solve():
    t = int(input())
    for _ in range(t):
        n, x, k = map(int, input().split())
        s = input().strip()  
        
        delta = [0] * (n + 1)
        for i in range(n):
            delta[i + 1] = delta[i] + (-1 if s[i] == 'L' else 1)
        
        m = None
        for i in range(1, n + 1):
            if delta[i] == 0:
                m = i
                break
        current_position = x
        index = 0  
        time = 0   
        hits = 0  
        
        while time < k:
            if index == n and current_position != 0:
                break
            if s[index] == 'L':
                current_position -= 1
            else:  # s[index] == 'R'
                current_position += 1
            time += 1
            index += 1
            
            if current_position == 0:
                hits += 1
                if m is not None:
                    rt = k - time
                    ah = rt // m
                    hits += ah
                    break
                else:
                    index = 0
        print(hits)

if __name__ == '__main__':
    solve()
# shakil_13_1027div3_c.py
import sys
import threading

def main():
    input = sys.stdin.readline
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        u = []
        l = None
        for x in a:
            if x != l:
                u.append(x)
                l = x       
            ans = 0
            bl = 1
        
        for i in range(1, len(u)):
            if u[i] == u[i-1] + 1:
                bl += 1
            else:
                ans += (bl + 1) // 2
                bl = 1
        ans += (bl + 1) // 2
        
        print(ans)
if __name__ == "__main__":
    threading.Thread(target=main).start()

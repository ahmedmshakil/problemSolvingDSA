# shakil_1005_div2
def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input().strip()
        if '1' not in s:
            print(0)
            continue
        transitions = 0
        for i in range(n-1):
            if s[i] != s[i+1]:
                transitions += 1
        if s[0] == '1':
            print(transitions + 1)
        else:
            print(transitions)
        
if __name__ == '__main__':
    solve()
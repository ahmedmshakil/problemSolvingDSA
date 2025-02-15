# shakil_13_codeforces1003_div4
def solve():
    s = input()
    n = len(s)
    has_consecutive = False
    for i in range(n - 1):
        if s[i] == s[i+1]:
            has_consecutive = True
            break
    if has_consecutive:
        print(1)
    else:
        print(n)

t = int(input())
for _ in range(t):
    solve()
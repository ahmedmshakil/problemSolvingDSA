# shakil_13_1017div3_e.py
def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        cnt = [0] * 30
        for num in a:
            for j in range(30):
                if num & (1 << j):
                    cnt[j] += 1
        ms = 0
        for k in range(n):
            cs = 0
            for j in range(30):
                if a[k] & (1 << j):
                    cs += (n - cnt[j]) * (1 << j)
                else:
                    cs += cnt[j] * (1 << j)
            ms = max(ms, cs)
        print(ms)

if __name__ == "__main__":
    solve()
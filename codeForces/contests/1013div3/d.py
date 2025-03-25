# shakil_13_1013div3_d.py
def solve():
    import sys
    input = sys.stdin.readline

    t = int(input().strip())
    for _ in range(t):
        n, m, k = map(int, input().split())
        def f(L):
            full_blocks = m // (L + 1)
            remainder = m % (L + 1)
            return full_blocks * L + min(L, remainder)
        
        low = 1
        high = m 
        ans = m
        
        while low <= high:
            mid = (low + high) // 2
            if n * f(mid) >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        print(ans)

if __name__ == "__main__":
    solve()

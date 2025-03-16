# 1009div3_by Shakil
def solve():
    import sys
    input = sys.stdin.readline
    
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        total = sum(arr)
        result = total - (n - 1)
        print(result)

if __name__ == "__main__":
    solve()

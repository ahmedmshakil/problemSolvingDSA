# shakil_13_1017div3_d.py
#   
#
# Set of possible positions in (s) after processing i hits from p.
# 1 >> hit produced a single sound
# 2 >> hit produced a double sound
def solve():
    import sys
    input = sys.stdin.readline

    t = int(input().strip())
    for _ in range(t):
        p = input().strip()
        s = input().strip()
        positions = {0}
        for char in p:
            next_positions = set()
            for pos in positions:
                if pos < len(s) and s[pos] == char:
                    next_positions.add(pos + 1)
                if pos + 1 < len(s) and s[pos] == char and s[pos + 1] == char:
                    next_positions.add(pos + 2)
            positions = next_positions
        if len(s) in positions:
            print("YES")
        else:
            print("NO")
if __name__ == "__main__":
    solve()

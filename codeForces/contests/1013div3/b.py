# shakil_13_1013div3_b.py
def solve():
    import sys
    input = sys.stdin.readline
    t = int(input().strip())
    results = []
    for _ in range(t):
        n, x = map(int, input().split())
        skills = list(map(int, input().split()))
        skills.sort(reverse=True)  
        
        teams = 0
        team_size = 0
        for skill in skills:
            team_size += 1
            if team_size * skill >= x:
                teams += 1   
                team_size = 0  
                
        results.append(str(teams))
        
    sys.stdout.write("\n".join(results))
    
if __name__ == '__main__':
    solve()

def solve():
    import sys
    input_data = sys.stdin.read().splitlines()
    
    n = int(input_data[0])
    x = 0
    for i in range(1, n + 1):
        statement = input_data[i]
        if "++" in statement:
            x += 1
        elif "--" in statement:
            x -= 1  
    print(x)

if __name__ == '__main__':
    solve()

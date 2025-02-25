# wrong answer in test 2

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t_index = 0
    t = int(data[t_index])
    t_index += 1
    results = []
    
    for _ in range(t):
        n, l, r = map(int, data[t_index:t_index+3])
        t_index += 3
        a = list(map(int, data[t_index:t_index+n]))
        t_index += n
        segment = a[l-1:r]
        outside = a[:l-1] + a[r:]
        
        segment.sort(reverse=True)  
        outside.sort()          
        i = 0
        j = 0
        while i < len(segment) and j < len(outside):
            if outside[j] < segment[i]:
                segment[i] = outside[j]
                i += 1
                j += 1
            else:
                break
        
        min_sum = sum(segment)
        results.append(str(min_sum))
    
    sys.stdout.write('\n'.join(results) + '\n')


if __name__ == '__main__':
    solve()
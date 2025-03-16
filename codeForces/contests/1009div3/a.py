# 1009div3_by Shakil
def can_form_square(l, r, d, u):
    return l == r and d == u and l == d

def solve_test_cases():
    t = int(input())
    results = []
    
    for _ in range(t):
        l, r, d, u = map(int, input().split())
        if can_form_square(l, r, d, u):
            results.append("Yes")
        else:
            results.append("No")
    
    return results

# Process test cases
if __name__ == "__main__":
    results = solve_test_cases()
    for result in results:
        print(result)
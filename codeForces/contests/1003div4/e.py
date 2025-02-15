def calculate_balance(s):
    max_balance = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j+1]
            zeros = substring.count('0')
            ones = substring.count('1')
            balance_value = max(zeros - ones, ones - zeros)
            max_balance = max(max_balance, balance_value)
    return max_balance

def solve():
    n, m, k = map(int, input().split())

    if k < abs(n - m):
        print("-1")
        return

    s = ""
    zeros_count = 0
    ones_count = 0

    for _ in range(n + m):
        appended = False
        if zeros_count < n:
            temp_s_0 = s + "0"
            if calculate_balance(temp_s_0) <= k:
                s = temp_s_0
                zeros_count += 1
                appended = True

        if not appended:
            if ones_count < m:
                temp_s_1 = s + "1"
                if calculate_balance(temp_s_1) <= k:
                    s = temp_s_1
                    ones_count += 1
                    appended = True
        
        if not appended: 
            print("-1")
            return

    if calculate_balance(s) == k:
        print(s)
    else:
        print("-1")


t = int(input())
for _ in range(t):
    solve()
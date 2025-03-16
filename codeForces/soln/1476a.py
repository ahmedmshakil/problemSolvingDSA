t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    min_sum = ((n + k - 1) // k) * k
    max_element = (min_sum + n - 1) // n

    print(max_element)

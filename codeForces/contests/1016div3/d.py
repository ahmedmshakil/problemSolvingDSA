# shakil_13_1016iv3_d.py
def get_number(k, s, x, y):
    if k == 1:
        if x == 1 and y == 1:
            return s
        elif x == 2 and y == 2:
            return s + 1
        elif x == 2 and y == 1:
            return s + 2
        elif x == 1 and y == 2:
            return s + 3
    else:
        m = 1 << (k - 1)  
        if x <= m and y <= m:
            return get_number(k - 1, s, x, y)

        else:
            return get_number(k - 1, s + 3 , x, y - m)

def get_position(k, s, d):
    if k == 1:
        if d == s:
            return (1, 1)
        elif d == s + 1:
            return (2, 2)
        elif d == s + 2:
            return (2, 1)
        elif d == s + 3:
            return (1, 2)
    else:
        size = 1 << (2 * k - 2)
        m = 1 << (k - 1)
        if d < s + size:
            x, y = get_position(k - 1, s, d)
            return (x, y)
        else:
            x, y = get_position(k - 1, s + 3 * size, d)
            return (x, y + m)

t = int(input())
for _ in range(t):
    n = int(input())
    q = int(input())
    for _ in range(q):
        query = input().split()
        if query[0] == "->":
            x, y = int(query[1]), int(query[2])
            print(get_number(n, 1, x, y))
        else:  # "<-"
            d = int(query[1])
            print(f"{x} {y}")
            
            
# WA on test case 1 according to CF
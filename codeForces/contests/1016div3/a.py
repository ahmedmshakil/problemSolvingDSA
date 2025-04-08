# shakil_13_1016iv3_a.py
# k is an ideal generator if and only if k is odd.
def is_ideal_generator(k):
    return k % 2 != 0
t = int(input().strip())

for _ in range(t):
    k = int(input().strip())
    if is_ideal_generator(k):
        print("YES")
    else:
        print("NO")

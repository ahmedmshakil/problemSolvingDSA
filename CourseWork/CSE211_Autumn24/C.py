n = int(input())
matrix = []
for i in range(0, n):
    matrix.append([int(i) for i in input().split()])
    
row_1 = 0 
col_1 = 0
row_2 = n -1 
col_2 = 0
sum_1 = 0
sum_2 = 0

for i in range(0, n):
    sum_1 += matrix[row_1 + i][col_1 + i]
    sum_2 += matrix[row_2 - i][col_2 + i]
    
print(abs(sum_1 - sum_2))

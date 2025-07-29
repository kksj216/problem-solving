n,m = map(int, input().split())

matrix_a = []
for i in range(n):
    matrix_a.append(list(map(int, input().split())))

matrix_b = []
for i in range(n):
    matrix_b.append(list(map(int, input().split())))

sum_m = [[0 for i in range(m)] for i in range(n) ]
for i in range(n):
    for j in range(m):
        sum_m[i][j] = matrix_a[i][j] + matrix_b[i][j]

for i in range(n):
    for j in range(m):
        print(sum_m[i][j], end=' ')
    print()

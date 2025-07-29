maps = [[0 for i in range(10)] for j in range(10)]

for i in range(9):
    maps[i+1] = [0] + list(map(int, input().split()))

# print(maps)
max_row = []
max_col = []
maximum = []
max_n = 0
for i in range(1, 10):
    for j in range(1, 10):
        if maps[i][j] >= max_n:
            max_n = maps[i][j]
            maximum.append(maps[i][j])
            max_row.append(i)
            max_col.append(j)

print(maximum[-1])
print(max_row[-1], max_col[-1])

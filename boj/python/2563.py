n = int(input())

paper = [[0]*100 for j in range(100)]

for i in range(n):
    x,y = map(int, input().split())

    for xx in range(x, x+10):
        for yy in range(y, y+10):
            paper[xx][yy] = 1

count = 0
for i in range(100):
    for j in range(100):
        if paper[i][j]==1:
            count += 1

print(count)
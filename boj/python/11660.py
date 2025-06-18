n, m = map(int, input().split())

maps = []
for i in range(n):
    a = list(map(int, input().split()))
    maps.append(a)

inputs = []
for i in range(m):
    a,b,c,d = map(int, input().split())
    inputs.append([[a,b], [c,d]])

dp = [[0 for _ in range(n+1)] for i in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + maps[i-1][j-1]
# print(dp)

results = []
for i in range(m):
    x1,y1 = inputs[i][0]
    x2,y2 = inputs[i][1]

    ans = dp[x2][y2]-dp[x1-1][y2]-dp[x2][y1-1]+dp[x1-1][y1-1]

    results.append(ans)

for i in results:
    print(i)



### 시간 초과 코드
"""
n, m = map(int, input().split())

maps = []
for i in range(n):
    a = list(map(int, input().split()))
    maps.append(a)

inputs = []
for i in range(m):
    a,b,c,d = map(int, input().split())
    inputs.append([[a,b], [c,d]])

ans = []
for i in range(m):
    dir1, dir2 = inputs[i][0], inputs[i][1]
    # print(dir1, dir2)

    count = 0
    for a in range(dir1[0]-1, dir2[0]):
        for b in range(dir1[1]-1, dir2[1]):
            count += maps[a][b]
    
    ans.append(count)

for i in ans:
    print(i)

"""



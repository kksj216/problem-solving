t = int(input())

ans = []

dp = [[0 for _ in range(30)] for _ in range(30)]
for i in range(1,30):
    for j in range(1,30):
        if i==1:
            dp[i][j] = j
        elif i==j:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i-1][j-1]+dp[i][j-1]


for i in range(t):
    n,m = map(int, input().split())
    
    ans.append(dp[n][m])

for i in ans:
    print(i)


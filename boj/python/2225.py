n,k = map(int, input().split())

dp = [[0]*(n+1) for i in range(k+1)]

for i in range(n+1):
    dp[1][i] = 1

if k > 1:
    for i in range(n+1):
        dp[2][i] = i+1

    for i in range(3,k+1):
        for j in range(n+1):
            dp[i][j] = dp[i][j-1] + dp[i-1][j]

print(dp[k][n] % 1000000000)

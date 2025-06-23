n,k = map(int, input().split())

coins = []
for i in range(n):
    coins.append(int(input()))

dp = [0 for i in range(k+1)]
dp[0] = 1

for coin in coins:
    for i in range(coin,k+1):
        dp[i] += dp[i-coin]

print(dp[k])

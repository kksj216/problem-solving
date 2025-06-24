n = int(input())

dp = [0 for i in range(n+1)]
wine = [0]

for i in range(n):
    wine.append( int(input()) )

dp[1] = wine[1]
if n > 2:
    dp[2] = wine[1]+wine[2]

    for i in range(3,n+1):
        dp[i] = max(dp[i-1], wine[i]+wine[i-1]+dp[i-3], wine[i]+dp[i-2])
elif n==2:
    dp[2] = wine[1]+wine[2]

print(max(dp))

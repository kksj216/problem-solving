n = int(input())

dp = [0 for i in range(n+1)]

if n==1:
    dp[1] = 0
    print(dp[n])

elif n==2:
    dp[2] = 1
    print(dp[n])

elif n==3:
    dp[3] = 1
    print(dp[n])

else:
    dp[1] = 0
    dp[2] = 1
    # dp[3] = 1
    for i in range(3, n+1):
        dp[i] = 1 + dp[i-1]
        if i % 3 == 0:
            dp[i] = min(dp[i], 1 + dp[i//3])
        if i % 2 == 0:
            dp[i] = min(dp[i], 1 + dp[i//2])
        # else:
        #     dp[i] = min(dp[i], 1 + dp[i-1])
        # else:
        #     dp[i] = 1 + dp[i-1]
    # print(dp)
    print(dp[n])

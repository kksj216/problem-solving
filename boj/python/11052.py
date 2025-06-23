n = int(input())
p_list = [0] + list(map(int, input().split()))

dp = [0 for i in range(n+1)]

for i in range(n+1):
    for j in range(i+1):
        dp[i] = max(dp[i], dp[i-j]+p_list[j])

print(dp[n])

print(dp)
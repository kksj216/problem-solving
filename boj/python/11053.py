n = int(input())

a_input = list(map(int, input().split()))

dp = [1 for i in range(n)]

for i in range(n):
    for j in range(i):
        if a_input[j] < a_input[i]:  # 부분적으로 증가
            dp[i] = max(dp[i], dp[j]+1)

# print(dp)

print(max(dp))
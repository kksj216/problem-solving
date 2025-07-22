n = int(input())

ls = []
for i in range(n):
    ls.append(list(map(int, input().split())))

ls.sort(key=lambda x:x[1])

dp = [1 for i in range(n)]

for i in range(1, n):
    for j in range(i):
        if ls[j][0] < ls[i][0]:
            dp[i] = max(dp[j]+1, dp[i])

# print(dp)
print(n - max(dp))

n = int(input())

arr = list(map(int, input().split()))
r_arr = arr[::-1]

dp = [1 for i in range(n)]

for i in range(1, n):
    for j in range(i):
        if r_arr[i] > r_arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

# print(dp)
print(max(dp))


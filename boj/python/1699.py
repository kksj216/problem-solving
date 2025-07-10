n = int(input())

dp = [i for i in range(n + 1)]


for i in range(1, n + 1):
    for j in range(1, i):
        if j*j>i:
            break
        if dp[i] > dp[i - j*j] + 1:
            dp[i] = dp[i-j*j]+1

print(dp[n])


# ''' 시간초과
# import math

# dp[0] =0
# dp[1] = 1
# dp[2] = 2
# dp[3] = 3

# for i in range(4, n + 1):
#     if i % math.sqrt(i) == 0:
#         dp[i] = 1
#     else:
#         dp[i] = float('inf')
#         for j in range(1, i//2+1):
#             dp[i] = min(dp[i], dp[j]+dp[i-j]) 

# print(dp[n])
# '''

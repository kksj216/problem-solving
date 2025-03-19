n = int(input())

arr_in = list(map(int, input().split()))

dp = [0]*n
dp[0] = arr_in[0]
for i in range(1, n):
    dp[i] = max(arr_in[i], arr_in[i]+dp[i-1])
    # 현재 값이 더 크다면 앞에 값을 더해 온 것은 의미가 없음 

# print(dp)
print(max(dp))
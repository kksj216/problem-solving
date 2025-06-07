n = int(input())

arr = [ list(map(int, input().split())) for _ in range(n)]
dp = [0]*(n+1)

for i in range(n-1, -1, -1):
    if i+arr[i][0]>n:  # i일 + 상담일 수 > 퇴사일 인 경우 
        dp[i] = dp[i+1]
    else:  # i일 상담하는 경우와 상담하지 않는 경우 중 큰 것으로
        dp[i] = max(dp[i+1], arr[i][1]+dp[i+arr[i][0]])

    # print(dp)


print(dp[0])
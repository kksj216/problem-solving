import sys

arr = []
dp = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]

input = sys.stdin.readline

'''
def go_w(a,b,c):
    if a <= 0 or b <= 0 or c <=0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return go_w(20, 20, 20)
    elif a < b and b < c:
        return go_w(a, b, c-1) + go_w(a, b-1, c-1) - go_w(a, b-1, c)
    else:
        return go_w(a-1, b, c) + go_w(a-1, b-1, c) + go_w(a-1, b, c-1) - go_w(a-1, b-1, c-1)
'''
def go_w_dp(a,b,c):
    if a <= 0 or b <= 0 or c <=0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return go_w_dp(20, 20, 20)
    
    if dp[a][b][c]:
        return dp[a][b][c]
    elif a < b and b < c:
        dp[a][b][c] = go_w_dp(a, b, c-1) + go_w_dp(a, b-1, c-1) - go_w_dp(a, b-1, c)
        return dp[a][b][c]
    else:
        dp[a][b][c] = go_w_dp(a-1, b, c) + go_w_dp(a-1, b-1, c) + go_w_dp(a-1, b, c-1) - go_w_dp(a-1, b-1, c-1)
        return dp[a][b][c]


while True:
    a, b, c = map(int, input().split())

    if a==-1 and b==-1 and c==-1:
        break

    res = go_w_dp(a,b,c)

    print("w({}, {}, {}) = {}" .format(a,b,c, res))

# print(arr)




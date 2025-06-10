str1 = str(input())
str2 = str(input())

dp = [[0 for _ in range(len(str2)+1)] for _ in range(len(str1)+1)]

for i in range(1, len(str1)+1):
    for j in range(1, len(str2)+1):

        if str1[i-1]==str2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1

        elif str1[i-1]!=str2[j-1]:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        # print(dp)

print(dp[len(str1)][len(str2)])


### LCS 값 구하기
a = len(str1)
b = len(str2)
ans = []
while (a>0 and b>0):
    if dp[a][b] == dp[a-1][b-1]+1:
        ans.append(str1[a-1])
        a -= 1
        b -= 1
    elif dp[a][b] == dp[a-1][b]:
        a -= 1
    elif dp[a][b] == dp[a][b-1]:
        b -= 1

result = ""
for i in range(len(ans)-1, -1, -1):
    result += ans[i]

print(result)
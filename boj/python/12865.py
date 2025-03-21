n, k = map(int, input().split())

mulgun = []
for i in range(n):
    mulgun.append((list(map(int, input().split()))))

# print(mulgun)
dp = [0 for i in range(k+1)]

for m in mulgun:
    weight, value = m[0], m[1]
    for i in range(k, weight-1, -1):
        dp[i] = max(dp[i], dp[i-weight]+value)

print(dp[-1])
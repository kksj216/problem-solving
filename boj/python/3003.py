chess = list(map(int, input().split()))
total = [1, 1, 2, 2, 2, 8]

ans = [0]*6
for i in range(6):
    ans[i] = total[i] - chess[i]
    print(ans[i], end=" ")

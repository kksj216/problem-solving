n = int(input())
arr = list(map(int, input().split()))

dp_up = [1 for i in range(n)]
dp_down = [1 for i in range(n)]

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:  # 부분 증가
            dp_up[i] = max(dp_up[i], dp_up[j]+1)

for i in range(n-1, -1, -1):  ## 감소는 거꾸로 뒤집어서 
    for j in range(n-1, i, -1):
        if arr[i] > arr[j]:  # 부분 감소
            dp_down[i] = max(dp_down[i], dp_down[j]+1)

# print("dp_up ", dp_up)
# print("dp down ", dp_down)

res = [0 for i in range(n)]
for i in range(n):
    res[i] = dp_up[i]+dp_down[i]-1

print(max(res))

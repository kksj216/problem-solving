n = int(input())
ns = list(map(int, input().split()))

m = int(input())
ms = list(map(int, input().split()))

dt = {}
for i in range(n):
    dt[ns[i]] = 0

# print(dt)

for i in range(m):
    if ms[i] not in dt:
        print(0, end=' ')
    else:
        print(1, end=' ')

N, M = map(int, input().split())

l = [0 for _ in range(M)]
basket = [0 for _ in range(N)]

for _ in range(M):
    i, j, k = map(int, input().split())

    for a in range(i-1, j):
        basket[a] = k

for i in basket:
    print(i, end=" ")

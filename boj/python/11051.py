N, K = map(int, input().split())

ressult = 1
for i in range(K):
    ressult *= N
    N -= 1

under = 1
k = K
for i in range(K):
    under *= k
    k -= 1

print((ressult//under)%10007)

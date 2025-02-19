n, m = map(int, input().split())

basket = [_+1 for _ in range(n)]

for _ in range(m):
    i, j = map(int, input().split())

    temp_i = basket[i-1]
    basket[i-1] = basket[j-1]
    basket[j-1] = temp_i

for i in basket:
    print(i, end=" ")

n, m = map(int, input().split())

basket = [i for i in range(n+1)]
for _ in range(m):
    i, j = map(int, input().split())

    if (j-i)%2!=0:
        for a in range(i, (i+j)//2+1):
            temp = basket[a]
            # basket[a] = basket[j-a+1]
            # basket[j-a+1] = temp
            basket[a] = basket[(i+j)-a]
            basket[(i+j)-a] = temp
    else:
        for a in range(i, (i+j)//2):
            if a == j:
                continue
            else:
                temp = basket[a]
                # basket[a] = basket[j-a+1]
                # basket[j-a+1] = temp
                basket[a] = basket[(i+j)-a]
                basket[(i+j)-a] = temp

for i in basket[1:]:
    print(i, end=" ")
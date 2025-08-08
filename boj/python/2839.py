n = int(input())

ls = []
for i in range(n):
    for j in range(n):
        if 3*i + 5*j == n:
            ls.append(i+j)
            break

if len(ls)==0:
    print(-1)
else:
    print(min(ls))

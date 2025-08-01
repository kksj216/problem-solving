n, k = map(int, input().split())

ls = [0]
for i in range(1,n+1):
    if n % i == 0:
        ls.append(i)

# print(ls)
if len(ls)-1 < k:
    print(0)
else:
    print(ls[k])

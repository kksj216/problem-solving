n = int(input())

ls = []
c = 2
while n > 1:
    if n%c == 0:
        n /= c
        ls.append(c)
    else:
        c += 1

# print(ls)
for i in ls:
    print(i)
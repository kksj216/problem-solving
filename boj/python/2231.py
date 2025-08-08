## 216 = 198 + 1 + 9 + 8

n = int(input())

ans = 0
for i in range(n):
    num = i
    num_ls = list(str(i))
    for j in range(len(num_ls)):
        num_ls[j] = int(num_ls[j])

    s = num+sum(num_ls)
    # print(num_ls)
    # print(s)

    if s == n:
        ans = i
        break
print(ans)
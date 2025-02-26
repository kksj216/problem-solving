n = int(input())
l = [[] for _ in range(n)]

for i in range(n):
    a, b = map(str, input().split())

    l[i] = [a,b]

# print(l)

for i in range(n):
    str = ""
    for j in range(len(l[i][1])):
        str += l[i][1][j]*int(l[i][0])
    print(str)
n = int(input())

name = []
for i in range(n):
    a, b = map(str, input().split())
    a = int(a)

    name.append((a,b))

# print(name)
name.sort(key=lambda x: x[0])
# print(name)

for i in range(n):
    print(name[i][0], name[i][1])
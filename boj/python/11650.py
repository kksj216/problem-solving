n = int(input())

n_list = []
for i in range(n):
    a, b = map(int, input().split())
    n_list.append((a,b))

# print(n_list)

n_list = sorted(n_list)

for i in n_list:
    print(i[0], i[1])

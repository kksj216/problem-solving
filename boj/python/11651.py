n = int(input())

n_list = []
for i in range(n):
    a, b = map(int, input().split())
    n_list.append((a,b))

n_list.sort(key=lambda x: (x[1],x[0]))

for i in n_list:
    print(i[0], i[1])

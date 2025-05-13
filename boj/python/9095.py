t = int(input())

n_list = []
for i in range(t):
    n_list.append(( int(input()) ))

# print(n_list)

dp_list = [0 for i in range(12)]
dp_list[1] = 1
dp_list[2] = 2
dp_list[3] = 4

for i in range(12):
    if i > 3:
        dp_list[i] = dp_list[i-1]+dp_list[i-2]+dp_list[i-3]

for i in n_list:
    print(dp_list[i])

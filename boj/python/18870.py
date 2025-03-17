n = int(input())

n_list = list(map(int, input().split()))

new_list = sorted(list(set(n_list)))

# for i in range(n):
#     for j in range(len(new_list)):
#         if n_list[i]==new_list[j]:
#             print(j, end=" ")

dic = {new_list[i] : i for i in range(len(new_list))}
# print(dic)
for i in n_list:
    print(dic[i], end = ' ')
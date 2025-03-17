import sys

n = int(sys.stdin.readline())

n_list = []
for _ in range(n):
    n_list.append(sys.stdin.readline().strip())

# print(n_list)
set_lst = set(n_list)  # 중복 제거!!!
# print(set_lst)
n_list = list(set_lst)
# print(n_list)

n_list.sort()
n_list.sort(key=lambda x: (len(x)))
# n_list.sort(key=len)

for i in n_list:
    print(i)

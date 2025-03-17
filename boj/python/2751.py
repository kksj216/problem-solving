import sys

n = int(sys.stdin.readline())

n_list = [0 for _ in range(n)]
for i in range(n):
    # n_list.append(int(input()))
    n_list[i] = int(sys.stdin.readline())

new_list = sorted(n_list) 

for i in new_list:
    print(i)
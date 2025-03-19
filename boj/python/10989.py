import sys

input = sys.stdin.readline
n = int(input())

## 메모리 초과
# arr = []
# for _ in range(n):
#     a = int(input())
#     arr.append(a)
# n_arr = sorted(arr)

# for i in range(n):
#     print(n_arr[i])

# ===================
arr = [0]*(10000+1)

for _ in range(n):
    arr [int(input())] += 1

for i in range(len(arr)):
    if arr[i] != 0:
        for _ in range(arr[i]):
            print(i)


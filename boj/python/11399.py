n = int(input())
arr = list(map(int, input().split()))

arr = sorted(arr)

# print(arr)

count = 0
for i in range(len(arr)):
    for j in range(i+1):
        count += arr[j]

print(count)
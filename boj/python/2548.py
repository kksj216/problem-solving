
n = int(input())
arr_input = list(map(int, input().split()))

arr_input.sort()

if len(arr_input)%2!=0:
    mid = len(arr_input)//2
else:
    mid = (len(arr_input)//2) - 1

print(arr_input[mid])

"""  => O(N^2)
arr = []
for i in range(len(arr_input)):
    count = 0
    for j in range(len(arr_input)):
        count += abs(arr_input[i] - arr_input[j])
    arr.append(count)

min_val = min(arr)
answer = []
for i in range(len(arr)):
    if min_val == arr[i]:
        answer.append(arr_input[i])

answer.sort()
print(answer[0])
"""

n = int(input())

arr = list(map(int, input().split()))

arr.sort()

### 투 포인터로 풀어야 함
left = 0
right = n-1

max_final = abs(arr[left] + arr[right])
result = [arr[left], arr[right]]

while left < right:
    max = arr[right]+arr[left]

    if abs(max) < max_final:
        result = [arr[left], arr[right]]
        max_final = abs(max)
        if max == 0:
            break
    if max < 0:
        left += 1
    else:
        right -= 1

print(result[0], result[1])
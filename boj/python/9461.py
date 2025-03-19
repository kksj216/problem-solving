t = int(input())

result = []
for i in range(t):
    n = int(input())

    arr = [1 for i in range(n+1)]

    if n > 3:
        arr[1] = 1
        arr[2] = 1
        arr[3] = 1
        for j in range(4,n+1):
            arr[j] = arr[j-2]+arr[j-3]

        result.append(arr[n])
    else:
        result.append(arr[n])

for j in result:
    print(j)


import sys

n = int(sys.stdin.readline())
arr = []
result = []
for i in range(n):
    a = sys.stdin.readline().split()
    a = a[0]
    arr.append(a)
    count = 0

    for j in range(len(a)):
        if a[j]=="(":
            count += 1
        else:
            count -= 1

        if count < 0:
            break
    
    if count == 0:
        result.append("YES")
    else:
        result.append("NO")

# print(result)
for r in range(len(result)):
    print(result[r])
import sys
# n = int(input())
n = int(sys.stdin.readline()) # input으로 하면 시간초과

arr = []
result = []
for i in range(n):
    order = sys.stdin.readline().split()
    
    if order[0]=="push":
        arr.append(int(order[1]))

    elif order[0]=="pop":
        if len(arr)==0:
            # print(-1)
            result.append(-1)
        else:
            # print(arr.pop())
            result.append(arr.pop())
    
    elif order[0]=="size":
        # print(len(arr))
        result.append(len(arr))
    
    elif order[0]=="empty":
        if len(arr)==0:
            # print(1)
            result.append(1)
        else:
            # print(0)
            result.append(0)
    
    elif order[0]=="top":
        if len(arr)==0:
            # print(-1)
            result.append(-1)
        else:
            # print(arr[-1])
            result.append(arr[-1])

for i in result:
    print(i)


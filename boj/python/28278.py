import sys

# n = int(input())
n = sys.stdin.readline().rstrip()

stacks = []
result = []
n = int(n)
for i in range(n):
    # a = list(map(int, input().split()))
    a =  list(sys.stdin.readline().strip().split(' '))
    # print('a: ',a) 

    a[0] = int(a[0])

    if a[0]==1:
        num = int(a[-1])
        stacks.append(num)

    elif a[0]==2:
        if len(stacks)>0:
            last = stacks.pop(-1)
            result.append(last)
            
        else:
            result.append(-1)

    elif a[0]==3:
        result.append(len(stacks))
    
    elif a[0]==4:
        if len(stacks)==0:
            result.append(1)
        else:
            result.append(0)
    
    elif a[0]==5:
        if len(stacks)>0:
            result.append(stacks[-1])
        else:
            result.append(-1)
    
for i in result:
    print(i)
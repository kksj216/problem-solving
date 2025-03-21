import sys

input = sys.stdin.readline

n = int(input())
stair = []
for i in range(n):
    stair.append(int(input()))

# print(stair)
xx = [0 for _ in range(n)]

if n<3:
    if n==1:
        xx[0] = stair[0]
    elif n==2:
        xx[1] = stair[0]+stair[1]
    print(xx[n-1])

else:
    xx[0] = stair[0]
    xx[1] = stair[0]+stair[1]
    xx[2] = max(stair[0]+stair[2], stair[1]+stair[2])

    for i in range(3,n):
        
        xx[i] = max(stair[i]+stair[i-1]+xx[i-3], stair[i]+xx[i-2])

    # print(xx)
    print(xx[n-1])


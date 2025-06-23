import sys
import heapq

n = int(input())

arr = []
for i in range(n):
    # x = int(input())
    x = int(sys.stdin.readline())

    if x==0:
        if len(arr)!=0:
            m = heapq.heappop(arr)
            print(m)
        else:
            print(0)
        
    else:
        heapq.heappush(arr,x)





'''
### 시간 초과
arr = []
ans = []
for i in x_list:
    if i==0:
        if len(arr)==0:
            ans.append(0)
        else:
            value = min(arr)
            arr.remove(value)
            ans.append(value)
    elif i>0:
        arr.append(i)

for i in ans:
    print(i)
'''

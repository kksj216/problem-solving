from collections import deque
import sys

input = sys.stdin.readline  ## 시간 초과

n,m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    a,b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

visited = [False for i in range(n+1)]
count = 0

for i in range(1,n+1):
    if visited[i]==False:

        ### BFS 수행 
        que = deque()
        que.append(i)

        visited[i]=True
        while que:
            cur = que.popleft()
            for j in graph[cur]:
                if visited[j]==False:
                    que.append(j)
                    visited[j]=True
        
        ### 연결된 노드 한번 돈 후 +=1
        count += 1

print(count)
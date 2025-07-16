from collections import deque
import heapq

n = int(input())
m = int(input())
buses = [[] for i in range(n+1)]
# value = [[0]*(n+1) for i in range(n+1)]
for i in range(m):
    a,b,c = map(int, input().split())
    buses[a].append((b,c))
    # buses[a].append(b)
    # value[a][b] = c

start, end = map(int, input().split())

### 다익스트라
dist = [int(1e9)]*(n+1)
dist[start] = 0
queue = []
heapq.heappush(queue, [dist[start], start])

while queue:
    count, node = heapq.heappop(queue)

    if dist[node] < count: # 기존 최단 거리보다 크면
        continue
    
    for next_node, next_dist in buses[node]:
        n = count + next_dist
        if n < dist[next_node]:
            dist[next_node] = n
            heapq.heappush(queue, [n, next_node])

# print(dist)
print(dist[end])

'''
### BFS로 풀면 메모리 초과
visited = [False for i in range(n+1)]

que = deque()
que.append(((start, [start], 0)))

visited[start] = True
result = []
minnum = float('inf')

while que:
    qpop = que.popleft()
    cur, lists, count = qpop[0], qpop[1], qpop[2]

    if cur==end:
        if count < minnum:
            minnum = count
            result.append([lists, count])

    for bus in buses[cur]:
        que.append((bus, lists+[bus], count+value[cur][bus]))
        visited[bus]=True

# print(result)
print(min(result, key=lambda x:x[1])[1])
'''
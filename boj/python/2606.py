from collections import deque

com_n = int(input())
net_n = int(input())

computer = [[] for _ in range(com_n+1)]

for i in range(net_n):
    a, b = map(int, input().split())
    computer[a].append(b)
    computer[b].append(a)
# print("computer: ", computer)

visited = [False for _ in range(com_n+1)]

que = deque([1])
visited[1] = True

count = 0

while que:
    com = que.popleft()

    for i in computer[com]:
        if not visited[i]:
            que.append(i)
            visited[i] = True
            count += 1  ## 여기에서 갯수 세기

print(count)

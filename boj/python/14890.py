n, l = map(int, input().split())

graph = [[] for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, input().split()))

print(graph)

for i in range(n):
    start = (0,i)  # 아래로 
    arr = []
    for i in range(n):
        arr.append()

    start = (i,0)  # 오른쪽으로 

    start = (n-1,i)  # 위로

    start = (0,n-1)  # 왼쪽으로 


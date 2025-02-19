N = int(input())
vec = list(map(int, input().split()))
v = int(input())

count = 0
for i in vec:
    if i == v:
        count += 1

print(count)
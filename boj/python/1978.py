n = int(input())
ls = list(map(int, input().split()))

count = 0

for l in ls:
    c = 0
    for k in range(1,l):
        if l%k==0:
            c += 1
    if c == 1:
        count += 1

print(count)
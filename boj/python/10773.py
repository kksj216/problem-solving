k = int(input())

ls = []
for i in range(k):
    ls.append( int(input()) )

stacks = []
for i in ls:
    if i != 0:
        stacks.append(i)
    if i == 0:
        stacks.pop(-1)

print(sum(stacks))
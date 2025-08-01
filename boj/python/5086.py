import sys

lists = []
while True:
    a,b = map(int, input().split())
    if a==0 and b==0: break
    else: lists.append([a,b])

for l in lists:
    if l[0]<l[1] and l[1]%l[0]==0:
        print("factor")
    elif l[0]>l[1] and l[0]%l[1]==0:
        print("multiple")
    else:
        print("neither")



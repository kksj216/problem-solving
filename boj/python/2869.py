A, B, V = map(int, input().split())

if A > V:
    print(1)
else:
    if (V-A)%(A-B)==0:
        print((V-A)//(A-B)+1)
    elif (V-A)%(A-B)!=0:
        print((V-A)//(A-B)+2)

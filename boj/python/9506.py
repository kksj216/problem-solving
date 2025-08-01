
ns = []
while True:
    n = int(input())
    if n==-1: break
    ns.append(n)

while ns:
    n = ns.pop(0)

    ls = []
    total = 0
    for i in range(1,n):
        if n%i==0:
            ls.append(i)
            total += i
    
    if total == n:
        print(f'{n} = ', end='')
        for j in ls:
            if j == ls[-1]:
                print(f'{j}')
            else:
                print(f'{j} + ', end='')
    else:
        print(f'{n} is NOT perfect.')

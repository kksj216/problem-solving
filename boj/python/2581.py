m = int(input())
n = int(input())

if m>n:
    print(-1)
    exit()
if (m==0 and n==0) or (m==1 and n==1):
    print(-1)
    exit()
    
if m==n:
    is_sosu = True
    for i in range(2, m):
        if m % i == 0: # 소수 아님
            is_sosu = False
            break
    
    if is_sosu==True:
        print(m)
        print(m)
        exit()
    else:
        print(-1)
        exit()
    
elif m < n:
    sosu_list = []
    for i in range(m,n+1):
        is_sosu = True  
        for j in range(2, i):
            if i % j == 0: # 소수 아님
                is_sosu = False
                break
                
        if is_sosu==True:
            sosu_list.append(i)
    
    if 0 in sosu_list:
        sosu_list.remove(0)
    if 1 in sosu_list:
        sosu_list.remove(1)



# print(sosu_list)
if len(sosu_list)==0:
    print(-1)
else:
    print(sum(sosu_list))
    print(min(sosu_list))
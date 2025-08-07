a,b,c = map(int, input().split())
s=[]
s.append(a)
s.append(b)
s.append(c)

if a==b==c:
    print(sum(s))
    exit()

max_n = max(s)
s.remove(max_n)
res = sum(s)

if max_n >= res:
    max_n = res-1
    
    s.append(max_n)
else:
    s.append(max_n)


print(sum(s))
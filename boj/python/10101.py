s = []
for i in range(3):
    s.append(int(input()))

if s[0]==s[1] and s[1]==s[2] and s[0]==s[2] and s[0]==60:
    print("Equilateral")
    exit()

if sum(s)==180:
    is_iso=False
    for i in range(3):
        if s.count(s[i])==2:
            is_iso=True
            break
    if is_iso==True:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")    
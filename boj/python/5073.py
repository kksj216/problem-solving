ans = []

while True:
    s = list(map(int, input().split()))
    if s[0]==0 and s[1]==0 and s[2]==0:
        break
    
    if s[0]==s[1]==s[2]:
        ans.append("Equilateral")
    else:

        is_iso=False
        for i in range(3):
            if s.count(s[i])==2:
                is_iso=True
                break
        
        if is_iso==True: # 두 변 같음
            max_n = max(s)
            s.remove(max_n)
            res = sum(s)

            if max_n >= res:
                ans.append("Invalid")
            else:
                ans.append("Isosceles")
            continue
        else: # 세 변 모두 다름
            max_n = max(s)
            s.remove(max_n)
            res = sum(s)

            if max_n >= res:
                ans.append("Invalid")
            else:
                ans.append("Scalene")
    
for i in ans:
    print(i)
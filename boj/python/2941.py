s = input()

arr = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
count = 0
# for i in range(len(s)):
i = 0
while i < len(s):
    
    if i+2 < len(s):
        s1 = s[i]+s[i+1]
        s2 = s[i]+s[i+1]+s[i+2]
        if s1 in arr:
            i += 2
            count += 1
        elif s2 in arr:
            i += 3
            count += 1
        elif s[i] not in arr:
            i += 1
            count += 1

    elif i+1 < len(s):
        s1 = s[i]+s[i+1]
        if s1 in arr:
            i += 2
            count += 1
        
        elif s[i] not in arr:
            i += 1
            count += 1
    
    elif s[i] not in arr:
        i += 1
        count += 1
print(count)
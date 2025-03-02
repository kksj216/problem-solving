n = int(input())

arrs = [""]*n

total = 0
for i in range(n):

    string = str(input())
    alp = [0]*26
    is_group = True

    for j in range(len(string)):
        if alp[ord(string[j]) - 97]!=0 and string[j]!=string[j-1]:
            is_group = False
            break
        else:
            alp[ ord(string[j]) - 97 ] += 1
    
    # if j == len(string)-1:
    #     print("aaa ", string)
    #     total += 1
    if is_group==True:
        # print("aaa ", string)
        total += 1

print(total)
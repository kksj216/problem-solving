s = input()

l = int(len(s))
ans = 1  # 길이 1인 경우 = 팰린드롬 True
if l%2!=0:  # 글자 수 홀수
    for i in range(l//2):
        if s[i] == s[l-(i+1)]:
            ans = 1
        else:
            ans = 0
            break
else:
    for i in range((l//2)):
        if s[i] == s[l-(i+1)]:
            ans = 1
        else:
            ans = 0
            break
print(ans)
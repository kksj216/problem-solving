a, b = map(int, input().split())
c = int(input())

if c > 59: # 1. 걸리는 시간이 1시간 이상이면 
    sum_a = (b+c)//60 # 몇 시간 추가인지
    sum_b = c%60 # 몇 분 추가인지

    a += sum_a
    b += sum_b
else: # 2. 걸리는 시간이 1시간 이내이면
    if (b+c)>59: # 2-1. 다음 hour 로 넘어갈 경우
        a += 1
        b = (b+c)-60
    else:  # 2-2. 지금 hour 내에서 분만 추가될 경우 
        b += c

if a > 23:
    a = a-24
if b > 59:
    b = b-60

print(a, b)
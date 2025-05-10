n = int(input())
arr = []
for i in range(n):
    a = list(map(int, input().split()))
    arr.append(a)

arr.sort(key=lambda x: (x[1],x[0]))  ## x[1]과 'x[0]' 도 필요함

count = 1
c = arr[0][1]  ## 0이 아닌 첫번째 회의의 끝나는 시간으로 
for i in range(1, n):  ## 0부터가 아니라 1번째 부터 시작하기
    if c <= arr[i][0]:  ## '<' 가 아닌 '<='
        count += 1
        c = arr[i][1]

print(count)
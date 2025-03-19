n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
    
new_arr = sorted(arr)

for i in range(n):
    print(new_arr[i])
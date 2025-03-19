arr = []
avg = 0
for _ in range(5):
    a = int(input())
    arr.append(a)
    avg += a

avg /= 5

new_arr = sorted(arr)
center = new_arr[2]

print(int(avg))
print(center)

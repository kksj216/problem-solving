n = int(input())

num = 1
count = 0
while True:
    num += 6*(count)

    if n <= num:
        count+=1
        break

    count += 1 
    
print(count)
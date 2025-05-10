in_str = str(input())

result = []
for i in range(1,len(in_str)):
    for j in range(i+1, len(in_str)):
        first = in_str[:i][::-1]
        second = in_str[i:j][::-1]
        third = in_str[j:][::-1]
        result.append(first+second+third)

result.sort()
print(result[0])

s = input()

count = 0
for i in s: 
    if 65<=ord(i)<=67: # 2
        count += 3
    elif 67<ord(i)<=70: # 3
        count += 4
    elif 70<ord(i)<=73: # 4
        count += 5
    elif 73<ord(i)<=76: # 5 
        count += 6
    elif 76<ord(i)<=79: # 6
        count += 7
    elif 79<ord(i)<=83: # 7
        count += 8
    elif 83<ord(i)<=86: # 8
        count += 9
    elif 86<ord(i)<=90: # 9
        count += 10

print(count)
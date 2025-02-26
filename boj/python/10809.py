s = input()

# a: 97
# z: 122
l = [-1 for _ in range(97, 123)]

for i in range(1, len(s)+1):
    l[ ord(s[len(s)-i]) - 97 ] = len(s)-i

for _ in l:
    print(_, end=" ")
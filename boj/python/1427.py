n = input()

l = list(n)
# for i in range(len(l)):
#     l[i] = int(l[i])

# print(l)

l = sorted(l, reverse=True)
print(''.join(l))

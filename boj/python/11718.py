# a = []
# while True:
#     if input() == True:
#         i = input()
#     if not i: break
#         a.append( i )

### Answer
while True:
    try:
        print(input())
    except EOFError:
        break

# import sys
# while True:
#     try:
#         print(sys.stdin.readline().rstrip())
#     except EOFError:
#         break
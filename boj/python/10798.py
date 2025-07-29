import sys

inputs = []
for i in range(5):
    inp = sys.stdin.readline().rstrip()
    inputs.append(inp)

max_n = max([len(i) for i in inputs])

lens = [len(i) for i in inputs]

strings = ""
for i in range(max_n):
    for j in range(5):
        if lens[j] <= i: continue
        strings += str(inputs[j][i])

print(strings)

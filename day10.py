with open('day10.txt') as f:
    adapters = [int(l) for l in f.read().split('\n')]
adapters = sorted(adapters)
differences = [0,0,0,0]
for i in range(len(adapters)-1):
    differences[adapters[i+1] - adapters[i]] += 1
print(adapters[0])
print((differences[1] + 1) * differences[3])
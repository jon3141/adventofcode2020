with open('day8.txt') as f:
	lines = f.read().split('\n')
program = []
for l in lines:
	program.append(l.split(' '))
acc = 0
current_line = 0
lines_visited = []
while current_line not in lines_visited:
	command = program[current_line][0]
	lines_visited.append(current_line)
	if command != 'jmp':
		if command == 'acc':
			acc += int(program[current_line][1])
		current_line += 1
	else:
		current_line += int(program[current_line][1])
print(acc)
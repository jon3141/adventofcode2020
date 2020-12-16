import math
with open('day5.txt') as f:
	lines = f.read().split('\n')
def get_location(seat_string):
	current_min = 0
	current_max = 127
	current_minx = 0
	current_maxx = 7
	diff = 128
	for i in range(7):
		diff /= 2
		if seat_string[i] == 'F':
			current_max -= diff
		elif seat_string[i] == 'B':
			current_min += diff
	row = int(current_max)
	diff = 8
	for i in range(3):
		diff /= 2
		if seat_string[i+7] == 'R':
			current_minx += diff
		elif seat_string[i+7] == 'L':
			current_maxx -= diff
	column = int(current_maxx)
	return [row, column]
def get_value(loc):
	return 8*loc[0] + loc[1]
values = [get_value(get_location(l)) for l in lines]
print(max(values))
for i in range(max(values)):
	if i+1 in values and i-1 in values and i not in values:
		print(i)


with open('day32020.txt') as f:
	lines = f.read().split('\n')
slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]
def check_slope(slope):
	current_pos = [0,0]
	hits = 0
	current_pos[1] += slope[1]
	while current_pos[1] < len(lines):
		current_pos[0] += slope[0]
		if current_pos[0] >= len(lines[0]):
			current_pos[0] -= len(lines[0])
		if lines[current_pos[1]][current_pos[0]] == '#':
			hits += 1
		current_pos[1] += slope[1]
	return hits
print(check_slope([3,1]))
sn = []
for s in slopes:
	sn.append(check_slope(s))
print(sn[0]*sn[1]*sn[2]*sn[3]*sn[4])
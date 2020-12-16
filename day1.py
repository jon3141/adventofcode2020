with open('day1.txt') as f:
	lines = f.read().split('\n')
ints = [int(l) for l in lines]
ints = sorted(ints)
def search_forward(start, do_three=False):
	result = 0
	if not do_three:
		for i in range(start+1, len(ints)):
			if ints[start] + ints[i] == 2020:
				result = ints[start] * ints[i]
				break
			elif ints[start] + ints[i] > 2020:
				break
	else:
		for i in range(start+1, len(ints)):
			search_for = 2020 - ints[start] - ints[i]
			if search_for > 0:
				if search_for in ints:
					result = ints[start] * ints[i] * ints[ints.index(search_for)]
					break
	return result
for i in range(len(ints)):
	test_var = search_forward(i)
	if test_var != 0:
		print(test_var)
		break
for i in range(len(ints)):
	test_var = search_forward(i, do_three=True)
	if test_var != 0:
		print(test_var)
		break
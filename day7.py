with open('day7.txt') as f:
	lines = f.read().split('\n')
all_bags = []
def parse_rule(r):
	parent = r.split(' contain ')[0]
	children = r.split(' contain ')[1].replace('.', '').split(', ')
	kids = {}
	for c in children:
		bag_type = ' '.join(c.split(' ')[1:])
		if bag_type not in all_bags:
			all_bags.append(bag_type)
		try:
			number = int(c.split(' ')[0])
			kids[bag_type] = number
		except:
			return {parent: None}
	return {parent: kids}
rules = {}
for l in lines:
	r = parse_rule(l)
	rules[list(r.keys())[0]] = r[list(r.keys())[0]]
can_holds = {}
def search_kids_for(current_key, bag_type):
	can_hold = False
	if current_key != bag_type and rules[current_key] is not None:
		for kid in rules[current_key].keys():
			if kid == bag_type:
				can_hold = True
			elif kid in can_holds:
				can_hold = can_holds[kid]
			elif kid in list(rules.keys()) and rules[kid] is not None:
				can_hold = search_kids_for(kid, bag_type)
	return can_hold
for r in rules:
	can_holds[r] = search_kids_for(r, 'shiny gold bags')
s = 0
for c in can_holds:
	if can_holds[c]:
		s += 1
print(s)
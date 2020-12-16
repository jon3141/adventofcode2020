with open('day6.txt') as f:
	groups = f.read().split('\n\n')
group_counts = []
def sp(word):
	return [char for char in word]
def get_group_count(g, e=False):
	members = g.split('\n')
	questions_answered = []
	if not e:
		for m in members:
			for q in m:
				if q not in questions_answered:
					questions_answered.append(q)
	else:
		all_answered = sp(members[0])
		for m in members:
			temp_answered = all_answered.copy()
			for q in all_answered:
				if q not in m:
					try:
						temp_answered.remove(q)
					except:
						pass
			all_answered = temp_answered
		questions_answered = all_answered
	return len(questions_answered)
for g in groups:
	group_counts.append(get_group_count(g))
print(sum(group_counts))
all_answered_groups = []
for g in groups:
	all_answered_groups.append(get_group_count(g, e=True))
print(sum(all_answered_groups))
with open('day2.txt') as f:
	lines = f.read().split('\n')
passwords = [{'criteria': l.split(': ')[0], 'password': l.split(': ')[1]} for l in lines]
correct_count = 0
alt_cc = 0
for p in passwords:
	nums, letter = p['criteria'].split(' ')
	low, high = nums.split('-')
	low = int(low)
	high = int(high)
	if p['password'].count(letter) >= low and p['password'].count(letter) <= high:
		correct_count += 1
	if (p['password'][low-1] == letter and p['password'][high-1] != letter) or (p['password'][low-1] != letter and p['password'][high-1] == letter):
		alt_cc += 1
print(correct_count)
print(alt_cc)
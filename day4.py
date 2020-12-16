with open('day4.txt') as f:
	passports = f.read().split('\n\n')
fields = sorted(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl','pid', 'cid'])
optional_fields = sorted(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl','pid'])
def parse_passport(passp):
	p = {}
	passp = passp.replace('\n', ' ')
	parts = passp.split(' ')
	for p1 in parts:
		p[p1.split(':')[0]] = p1.split(':')[1]
	return p
ps = []
for passp in passports:
	ps.append(parse_passport(passp))
correct_count = 0
def verify_passport(pas, verify_fields=False):
	any_not_in = True
	p = list(pas.keys())
	for f in optional_fields:
		if f not in p:
			any_not_in = False
			break
	if any_not_in and verify_fields:
		valid = True
		if int(pas['byr']) < 1920 or int(pas['byr']) > 2002:
			valid = False
		if int(pas['iyr']) < 2010 or int(pas['iyr']) > 2020:
			valid = False
		if int(pas['eyr']) < 2020 or int(pas['eyr']) > 2030:
			valid = False
		if 'cm' in pas['hgt'] or 'in' in pas['hgt']:
			if 'cm' in pas['hgt']:
				if int(pas['hgt'][0:-2]) < 150 or int(pas['hgt'][0:-2]) > 193:
					valid = False
			elif 'in' in pas['hgt']:
				if int(pas['hgt'][0:-2]) < 59 or int(pas['hgt'][0:-2]) > 76:
					valid = False
		if 'cm' not in pas['hgt'] and 'in' not in pas['hgt']:
			valid = False
		valid_chars = '0123456789abcdef'
		def check_hcl(hcl):
			thcl = hcl[1:]
			for h in hcl:
				if h not in valid_chars:
					return False
			return True
		if '#' not in pas['hcl'] or len(pas['hcl']) != 7 or not check_hcl(pas['hcl']):
			valid = False
		valid_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
		if pas['ecl'] not in valid_colors:
			valid = False
		if len(pas['pid']) != 9:
			valid = False
		try:
			int(pas['pid'])
		except:
			valid = False
		any_not_in = valid
	return any_not_in
for p in ps:
	if verify_passport(p):
		correct_count += 1
print(correct_count)
verified = 0
for p in ps:
	if verify_passport(p, verify_fields=True):
		verified += 1
print(verified)

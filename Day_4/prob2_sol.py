file = open('passports.txt').read().split('++++++') 

def haircolor(h):
	return ord('0') <= ord(h) <= ord('9') or ord('a') <= ord(h) <= ord('f') 
#given requirements to be considered as a valid passport
def givenfield(a,b):
	if a == 'byr':
		return b.isnumeric() and 1920 <= int(b) <= 2002

	if a == 'iyr':
		return b.isnumeric() and 2010 <= int(b) <= 2020
	if a == 'eyr':
		return b.isnumeric() and 2020 <= int(b) <= 2030
	if a == 'hgt':
		if b[-2:] == 'cm':
			return b[:-2].isnumeric() and 150 <= int(b[:-2]) <= 193
		if b[-2:] == 'in':
			return b[:-2].isnumeric() and 59 <= int(b[:-2]) <= 76
		return False
	if a == 'hcl':
		return b[0] == '#' and all([haircolor(b[i]) for i in range(1,len(b))])
	if a == 'ecl':
		return b in 'amb blu brn gry grn hzl oth'.split()
	if a == 'pid':
		return len(b)==9 and b.isnumeric()
	if a == 'cid':
		return True
	return False



count = 0
for x in file:
	d = {}
	for y in x.split():
		a,b = y.split(':')
		d[a] = b
	if len(d) == 8 and all([givenfield(k,d[k]) for k in d]):
		count += 1
	elif len(d) ==7 and 'cid' not in d and all([givenfield(k,d[k])for k in d]):
		count += 1
print(count)

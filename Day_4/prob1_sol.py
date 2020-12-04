file = open('passports.txt').read().split('++++++') #replaced empty lines with ++++++ in sublime and splited using that
count = 0
for x in file: 
	d = {}             #create empty dictionary
	for y in x.split():    
		a,b = y.split(':')   #split two words with ':' and store in a and b
		d[a] = b       # here a is key and b is value  
	if len(d) == 8:    # if the dictionary conists all the parameters then increment count
		count += 1
	elif len(d) ==7 and 'cid' not in d:    #we can ignore cid 
		count += 1
print(count)

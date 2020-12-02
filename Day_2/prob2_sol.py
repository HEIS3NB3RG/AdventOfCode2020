file = open('passwords','r')
valid_password = 0
all_elements = []

for i in file.readlines():
    takeout_colon = i.split(':')
    password = takeout_colon[1]
    takeout_space=takeout_colon[0].split(' ')
    takeout_dash=takeout_space[0].split('-')
    all_dict = {'low': int(takeout_dash[0]),'high':int(takeout_dash[1]),'characters':takeout_space[1],'password':takeout_colon[1]}
    all_elements.append(all_dict)
total_count = 0
for j in all_elements:
     if ( ( j["password"][j["low"]] == j["characters"]) ) ^ ( (j["password"][j["high"]] == j["characters"] ) ):
            total_count += 1
        
print(total_count)         

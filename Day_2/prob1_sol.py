
file = open('passwords','r')
valid_password = 0
for i in file:
    takeout_colon = i.split(':')
    password = takeout_colon[1]
    takeout_space=takeout_colon[0].split(' ')
    character = takeout_space[1]
    takeout_dash=takeout_space[0].split('-')
    lower_value=takeout_dash[0]
    higher_value=takeout_dash[1]
    
    if int(lower_value)<=password.count(character)<=int(higher_value):
        valid_password += 1
        
        
print(valid_password)

        
    
    
    
    

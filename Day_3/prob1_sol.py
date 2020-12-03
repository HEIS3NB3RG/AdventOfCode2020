with open('hashes') as file:    
    lines = file.readlines()  #read lines one by one
    map = [line.strip() for line in lines]   #eliminate the whitespaces
tree_count = 0  #initialize tree_count to 0
dx,dy = 0,0     #initialize dx and dy to 0,0
while dx+1 < len(map):   #while loop
    dx += 1   #for part2 change the rows here
    dy += 3   #for part2 change the columns here
    element = map[dx][dy % len(map[dx])] #finding the tree('#') 
    if element == '#':  #if the element is equal to #
        tree_count += 1  #count it
print(tree_count)   #display the count

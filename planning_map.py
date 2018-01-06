global row_SIZE 
global col_SIZE 
global MAP_AREA 
global FREE 
global OBST 
global GOAL 
global world_map 
global start 
global goal

col_SIZE = 5
row_SIZE = 4
MAP_AREA = 20
FREE = 0
OBST = 1
GOAL = 2

'''A list of 4 lists each representing a new row, and
item at each index of every list represent a column'''
world_map = [[0, 0, 0, 0, 0],
		[0, 0, 1, 1, 0],
		[0, 0, 1, 0, 0],
		[0, 1, 0, 0, 0]]  
start = [1, 2] # list of 2 values [c,r]
goal = [4, 3] # list of 2 values [c,r]

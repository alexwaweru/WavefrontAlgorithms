from planning_map import *

global map_space
map_space = world_map # Map of the entire space

def set_goal():
    goal_row = goal[1]
    goal_col = goal[0]
    map_space[goal_row][goal_col] = 2

def get_neighbours(cell): 
    neighbours = []
    rows = [cell[1]-1, cell[1], cell[1]+1] # All possible rows
    cols = [cell[0]-1, cell[0], cell[0]+1] # All possible cols
    '''Combining rows and cols to get all possible cells'''
    for r in rows:
        if (r < row_SIZE and r >= 0): # Checks if the cell is at the edge
            for c in cols:
                if (c < col_SIZE and c >= 0): # Checks if the cell is at the edge
                    if ((r!=cell[1]-1 and r!=cell[1]+1) or (c!=cell[0]-1 and c!=cell[0]+1)): 
                            neighbour = [c,r]
                            '''Make sure all cells conform to 4-point (and not 8-point) connectivity '''
                            if (neighbour!=[cell[0], cell[1]]): # Remove the current cell from the neighbours list
                                neighbours.append(neighbour)
    return neighbours

def breadth_first():
    
    queue = []
    queue.append(goal)

    while len(queue)!=0:
        cell = queue.pop(0)
        neighbours = get_neighbours(cell)
        for i in range(len(neighbours)):
            if map_space[neighbours[i][1]][neighbours[i][0]] == 0:
                map_space[neighbours[i][1]][neighbours[i][0]] = map_space[cell[1]][cell[0]] + 1
                queue.append(neighbours[i])

set_goal()
breadth_first()
    
 
            
        
        
    
    
    
    
    

    
    

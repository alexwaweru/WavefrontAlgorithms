from planning_map import *
from wvfrnt_algorithmns import*
##from move import*

global current_pos
global current_dir
global neighbours
global current_row
global current_col
global final_path_cells
global final_path_directions
global navigation_plan

current_pos = start # list of 2 values [c,r]
current_dir = 1 # 1 =up, 2=right, 3=down, 4=left
current_col = current_pos[0] # The column of the start cell
current_row = current_pos[1] # The row of the start cell
neighbours = [] #An empty list of cells
next_cell=[]
navigation_plan = []
'''The final path is a double linked list with each node connected
to a prev and next node
'''
final_path_cells = []
final_path_cells.append(current_pos)
final_path_directions = []
final_path_directions.append(current_dir)


def get_neighbours():
    global current_dir # The current direction of the robot
    global neighbours # The list of neighbouring cells
    global current_row # The row of the current cell
    global current_col # The column of the current cell
    global final_path # The final_path containing all the cell one after the other

    rows = [current_row-1, current_row, current_row+1] # All possible rows
    cols = [current_col-1, current_col, current_col+1] # All possible cols
    '''Combining rows and cols to get all possible cells'''
    for r in rows:
        if (r < row_SIZE and r >= 0): # Checks if the cell is at the edge
            for c in cols:
                if (c < col_SIZE and c >= 0): # Checks if the cell is at the edge
                    if ((r!=current_row-1 and r!=current_row+1) or (c!=current_col-1 and c!=current_col+1)): 
                            neighbour = [c,r]
                            '''Make sure all cells conform to 4-point (and not 8-point) connectivity '''
                            if (neighbour!=[current_col, current_row]): # Remove the current cell from the neighbours list
                                neighbours.append(neighbour)
    return neighbours


def get_next_cell():
    global current_pos
    global current_row
    global current_col
    global final_path
    global neighbours
        
    for i in range(len(neighbours)):
        r = int(neighbours[i][0]); c = int(neighbours[i][1])
        if map_space[c][r] == map_space[current_row][current_col] - 1:
            final_path_cells.append(neighbours[i])
            current_pos = neighbours[i]
            current_col = current_pos[0]
            current_row = current_pos[1]

    '''Append the next direction to the directions list'''
    prev_cell = final_path_cells[-2]
    current_cell = final_path_cells[-1]

    if (prev_cell[0] == current_col - 1): #moved right
        final_path_directions.append(2)
    if (prev_cell[0] == current_col + 1): #moved left
        final_path_directions.append(4)
    if (prev_cell[1] == current_row - 1): #moved down
        final_path_directions.append(3)
    if (prev_cell[1] == current_row + 1): #moved up
        final_path_directions.append(1)

    neighbours = [] #Reset neighbour to an empty list        
    return final_path_cells, final_path_directions


def generate_path():
    global current_pos
    global current_dir
    global neighbours
    global current_row
    global current_col
    global final_path_cells
    
    while not (current_col == goal[-2] and current_row == goal[-1]):
        get_neighbours()
        get_next_cell()


def navigate():
    global navigation_plan

    for i in range(1, len(final_path_directions)):
        angle = (final_path_directions[i] - final_path_directions[i-1])*90
        navigation_plan.append(angle)
    return navigation_plan

def drive():
    global navigation_plan
    
    generate_path()
    navigate()

    for i in navigation_plan:
        drive_straight(47)
        turn_right(i+1) #for cases where the angle is 0

drive()



 
        



import math
import heapq
import sys
import itertools

#TODO clean up
#TODO add solution to units clipping. Add a penalty to score for occupying units
GRID_STEP = 0.25
GRID_SIZE = 40
def xrange(start,stop, step=1.0):
    while start < stop:
        yield float(start)
        start +=step

def round_closest(num, closest=0.5):
    return float( closest * round( num / closest ))

def round_to_grid(cords):
    x = round_closest(cords[0], GRID_STEP)
    y = round_closest(cords[1], GRID_STEP)
    return x,y 
    
class Grid:
    def __init__(self):
        self.cells = {} #str_key : Cell
        
        for x in xrange(0,GRID_SIZE+GRID_STEP,GRID_STEP):
            for y in xrange(0,GRID_SIZE+GRID_STEP,GRID_STEP):
                self.cells['{},{}'.format(x,y)]=GridCell(x,y)
        for x in xrange(0,GRID_SIZE+GRID_STEP,GRID_STEP):
            for y in xrange(0,GRID_SIZE+GRID_STEP,GRID_STEP):
                cell = self[[x,y]]
                #get 4 adjacent cells
                if x > 0:
                    cell.adjacent.append(self[[x-GRID_STEP,y]])
                    if y > 0:
                        cell.adjacent.append(self[[x-GRID_STEP,y-GRID_STEP]])
                    if y < GRID_SIZE:
                        cell.adjacent.append(self[[x-GRID_STEP,y+GRID_STEP]])
                if x < GRID_SIZE:
                    cell.adjacent.append(self[[x+GRID_STEP,y]])
                    if y > 0:
                        cell.adjacent.append(self[[x+GRID_STEP,y-GRID_STEP]])
                    if y < GRID_SIZE:
                        cell.adjacent.append(self[[x+GRID_STEP,y+GRID_STEP]])
                if y > 0:
                    cell.adjacent.append(self[[x,y-GRID_STEP]])
                if y < GRID_SIZE:
                    cell.adjacent.append(self[[x,y+GRID_STEP]])
                
                cell.towers_firing = get_towers_firing_at_cords([cell.x, cell.y])
                
                
    def print_grid(self):
        grid = []

        for x in xrange(0,GRID_SIZE+GRID_STEP,GRID_STEP):
            row = []
            for y in xrange(0,GRID_SIZE+GRID_STEP,GRID_STEP):
                row.append(self[[x,y]])
            grid.append(row)
        return '\n'.join(['|'.join([ ' '*(6-len(str(round(cell.distance,3))))+ str(round(cell.distance,3) ) for cell in row]) for row in grid])

    def __getitem__(self, cords):
        x, y = round_to_grid(cords)
        return self.cells['{},{}'.format(x,y)]
        

class GridCell:
    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.adjacent = []
        self.towers_firing = []#get_towers_fiting_at_cords(self.cords)
        
        self.color = 'white'
        self.distance = 9999999
        self.preceedor = None
    
    @property
    def cords(self):
        return [self.x, self.y]

    def __repr__(self):
        return 'Cell {},{}'.format(self.x, self.y)
            
    def __str__(self):
        return 'Cell {},{}'.format(self.x, self.y)
        
    def __gt__(self, other):
        return self.distance > other.distance
        
def euclidean(cord1, cord2):
    return math.sqrt((cord2[0]-cord1[0])**2 + (cord2[1]-cord1[1])**2)

def manhattan(cord1, cord2):
    return abs(cord2[0]-cord1[0]) + abs(cord2[1]-cord1[1])
    
def get_towers_firing_at_cords(cords):
    return []

def safest_path(start_point, end_point):
    #Use A* algorithm. A paths weight equals the amount of towers firing at it.
    #init everything
    for cords, cell in grid.cells.items():
        cell.distance = 9999999
        cell.preceedor = None
    i=0
    start_point.distance = 0
    queue = [start_point] #priority queue, items with least distance get popped first
    while queue:
        i+=1
        cell = heapq.heappop(queue)
        if cell == end_point:
            break
        
        for adj in cell.adjacent:
            #get distance to cell
            base = cell.distance
            g = base+1+sum([tower['damage_per_shot']*tower['rate_of_fire'] for tower in adj.towers_firing])
            h = euclidean([adj.x, adj.y],[end_point.x, end_point.y]) #heuristic
            newdist =g+h
            if newdist < adj.distance:
                adj.distance = newdist
                adj.preceedor = cell
                heapq.heappush(queue, adj)
                
    #Seek pruned path
    path = []
    cell = end_point
    prev = None
    last_direction = None
    while cell:
        if prev:
            #if only x changed, only y changed or both changed since prev node we don't add this node to pruned
            change = [abs(cell.x-prev.x), abs(cell.y-prev.y)]
            direction=None
            if change[0] and not change[1]:
                direction='x'
            if change[1] and not change[0]:
                direction='y'
            if change[1] and change[0]:
                direction='xy'
            if last_direction and direction != last_direction:
                path.append([prev.x, prev.y])
            last_direction = direction
        else:
            path.append([cell.x, cell.y])
        prev = cell
        cell = cell.preceedor
        if not cell:
            path.append([prev.x, prev.y])
            
        
    return path[::-1]


grid = Grid()
path = []


from battle import commander
from battle import ROLE
import math
import heapq
import sys
import itertools
unit_client = commander.Client()

#TODO clean up
#TODO add solution to units clipping. Add a penalty to score for occupying units
GRID_STEP = 1
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
    towers = []
    all_towers = unit_client.ask_towers()
    for tower in all_towers:
        tower_cords = tower['coordinates']
        tower_range = tower['firing_range']
        
        if euclidean(cords, tower_cords) <= tower_range+1:
            towers.append(tower)
    return towers

def get_closest_next_of_path(path, cords):
    closest_i = None
    closest = None
    min_dist = None
    for i, crd in enumerate(path):
        dist = euclidean(crd, cords)
        if not min_dist or dist < min_dist:
            min_dist = dist
            closest = crd
            closest_i = i
    if closest_i+1 < len(path):
        return path[closest_i+1]
    return None
    
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
        
def attack_enemy(*args, **lwargs):
    enemies = unit_client.ask_my_range_enemy_items()
    enemy = None
    if weakest_tower_target:
        for item in enemies:
            if item['id'] == weakest_tower_target['id']:
                enemy = item
                break
    if not enemy:
        for item in enemies:
            if item['role'] == ROLE.BUILDING:
                enemy = item
                break
    
    if enemy['role']==ROLE.BUILDING:
        blocking = False
        #only attack if its blocking our path
        size = enemy['size']+0.5
        closest = get_closest_next_of_path(path, unit_client.ask_my_info()['coordinates'])

        for node in path:
            if euclidean(node, enemy['coordinates']) < size:
                blocking = True
                break
        
        if not blocking:
            enemy = None
        
    if enemy:
        unit_client.do_attack(enemy['id'])
        
        if enemy['id'] == weakest_tower_target['id']: 
            unit_client.when_item_destroyed(enemy['id'], on_tower_destroyed)
    else:
        decision()

def on_tower_destroyed(*args, **kwargs):
    global tower_destroyed
    global weakest_tower_target
    weakest_tower_target = None
    tower_destroyed = True
    rush_safest_path()

def rush_safest_path(*args, **kwargs):
    global path
    my_id = unit_client.ask_my_info()['id']
    unit_cords = unit_client.ask_my_info()['coordinates']
    command_center_cords = unit_client.ask_center()['coordinates']
    path = safest_path(grid[unit_cords], grid[command_center_cords])
    unit_client.when_enemy_in_range(attack_enemy)
    unit_client.do_moves(path)

#Get weakest tower

def get_weakest_tower(): #return all towers with min power
    all_towers = unit_client.ask_towers()
    #tower_power = num_of_other_towers_around + firing_range + hit_points + damage_per_shot * rate_of_fire

    towers = []
    def calc_power(tower):
        #normed values
        firing_range = tower['firing_range'] / 40
        hit_points = tower['hit_points'] / 5000
        dps = tower['damage_per_shot'] * tower['rate_of_fire'] / 2500
        other_towers = len(grid[tower['coordinates']].towers_firing) / 5
        print(tower)
        print("other_towers", "firing_range", "hit_points", "dps")
        print(other_towers, firing_range, hit_points, dps)
        return other_towers + firing_range + hit_points + dps

    weakest_power = None
    for tower in all_towers:
        power = calc_power(tower)
        if not weakest_power:
            weakest_power = power
        elif power < weakest_power:
            towers = [tower]
        elif power == weakest_power:
            towers.append(tower)

    return towers

def rush_weakest_tower(*args, **kwards):
    global weakest_tower_target
    weakest = get_weakest_tower()
    unit_cords = unit_client.ask_my_info()['coordinates']
    closest = min(weakest, key=lambda t: euclidean(unit_cords, tower['coordinates']))
    weakest_tower_target = closest
    tower_cords = closest['coordinates']
    path = safest_path(grid[unit_cords], grid[tower_cords])
    unit_client.when_enemy_in_range(attack_enemy)
    unit_client.do_moves(path)

def decision(*args, **kwargs):
    #just destroy one tower, weakest, then go for the center

    #todo add check if its safe to proceed to center
    #actually this can easily be done by checking if any tiles on path ahead are under turret fire
    if tower_destroyed:
        rush_safest_path()
    else:
        rush_weakest_tower()

weakest_tower_target = None
tower_destroyed = False
grid = Grid()
path = []

decision()



class Vertex:

    def __init__(self, key, connections = None):
        self.key = key
        self.connections = connections or {}
        self.color = 'white'
        self.preceedor = None
        self.distance = None
        self.visited = False

    def add_edge(self, vertex, weight=0):
        self.connections[vertex] = weight

    def get_connections(self):
        return self.connections.keys()

    def __repr__(self):
        return str(self.key)# + ' connected to ' + str([v.key for v in self.get_connections()])

class Graph:
    def __init__(self, vertexes = None):
        self.vertexes = vertexes or {}

    def get_or_create_vertex(self, key):
        if not key in self.vertexes:
            self.vertexes[key] = Vertex(key)

        return self.vertexes[key]

    def __contains__(self, key):
        return key in self.vertexes

    def __iter__(self):
        return iter(self.vertexes.values())

    def __getitem__(self, key):
        if key in self.vertexes:
            return self.vertexes[key]

    def add_vertex(self, key, connected_to = []): #connected_to = [ (key, weight) ]
        connections = {}
        for k, weight in connected_to:
            vertex = self.get_or_create_vertex(k)
            connections[vertex] = weight
        vertex = Vertex(key, connections)
        self.vertexes[key] = vertex

    def add_edge(self, key1, key2, weight=0):
        vertex1 = self.get_or_create_vertex(key1)
        vertex2 = self.get_or_create_vertex(key2)

        vertex1.add_edge(vertex2, weight)


g = Graph()


# for i in range(6):
#     g.add_vertex(i)



g.add_edge(0,1,5)
g.add_edge(0,5,2)
g.add_edge(1,2,4)
g.add_edge(2,3,9)
g.add_edge(3,4,7)
g.add_edge(3,5,3)
g.add_edge(4,0,1)
g.add_edge(5,4,8)



""" Word ladder problem

Transform the word “FOOL” into the word “SAGE”. In a word ladder puzzle you must make the change occur gradually by changing one letter at a time. At each step you must transform one word into another word, you are not allowed to transform a word into a non-word. The word ladder puzzle was invented in 1878 by Lewis Carroll, the author of Alice in Wonderland. The following sequence of words shows one possible solution to the problem posed above.

FOOL
POOL
POLL
POLE
PALE
SALE
SAGE

"""
g = Graph()
words = ["FOOL", "POOL", "POLL", "POLE", "PALE", "SALE", "SAGE"]
#Bucket the words that differ by one letter
buckets = {}
for word in words:
    for i in range(len(word)):
        bucket = word[:i]+'_'+word[i+1:]
        if bucket in buckets:
            buckets[bucket].append(word)
        else:
            buckets[bucket] = [word]
    

for bucket in buckets.values():
    #All words in a bucket should be connected
    for word in bucket:
        for other_word in bucket:
            if word != other_word:
                g.add_edge(word, other_word)


def bfs(graph, s, target):
    s.distance = 0
    s.color = 'grey'
    s.preceedor = None
    discovered = [s] #queue
    while discovered:
        node = discovered.pop()
        connections = node.get_connections()
        for connection in connections:
            print('exploring connection', connection)
            if connection.color == 'white':
                connection.preceedor = node
                connection.color = 'grey'
                connection.distance = connection.preceedor.distance+1
                discovered.append(connection)
        node.color = 'black'
    #return path to target
    path = []
    end_node = graph[target]
    while end_node:
        path.append(end_node)
        end_node = end_node.preceedor

    return path

#print(bfs(g, g['POLE'], 'SAGE'))


""" The knights tour problem 

Another classic problem that we can use to illustrate a second common graph algorithm is called the “knight’s tour.” 
The knight’s tour puzzle is played on a chess board with a single chess piece, the knight. 
The object of the puzzle is to find a sequence of moves that allow the knight to visit every square on the board exactly once. 
One such sequence is called a “tour.” The knight’s tour puzzle has fascinated chess players, mathematicians and computer scientists alike for many years. 
The upper bound on the number of possible legal tours for an eight-by-eight chessboard is known to be 1.305×10351.305×1035; however, there are even more possible dead ends. 
Clearly this is a problem that requires some real brains, some real computing power, or both.

Although researchers have studied many different algorithms to solve the knight’s tour problem, a graph search is one of the easiest to understand and program. 
Once again we will solve the problem using two main steps:
- Represent the legal moves of a knight on a chessboard as a graph.
- Use a graph algorithm to find a path of length rows×columns−1rows×columns−1 where every vertex on the graph is visited exactly once.


"""

def pos_to_id(x, y, N):
    return x+N*y

def gen_knight_graph(N): #A graph of legal moves for a knight figure
    g = Graph()
    for x in range(N):
        for y in range(N):
            #each pos is a vertex
            legal_moves = gen_legal_moves(x, y, N)
            for move in legal_moves:
                #convert each move to a graph
                g.add_edge(pos_to_id(x,y,N), pos_to_id(move[0], move[1], N))
    return g

def gen_legal_moves(x, y, N):
    moves = []
    offsets = [(-1, -2), (1, -2), (2, -1), (-2, -1), (2, 1), (-2, 1), (1, 2), (-1, 2)]

    for offset in offsets:
        new_x = x + offset[0]
        new_y = y + offset[1]
        if new_x >= 0 and new_x < N and new_y >= 0 and new_y < N:
            moves.append([new_x,new_y])
    return moves

g = gen_knight_graph(3)

def dfs(graph, start): #wrong: reaches first deadend and dies
    cur_node = start
    visited = []
    while cur_node:
        cur_node.visited = True
        visited.append(cur_node.key)
        connections = [connection for connection in cur_node.get_connections() if not connection.visited == True]
        if not connections:
            return visited
        else:
            cur_node = connections[0]

#print(dfs(g, g[0]))
def knightTour(n,path,u,limit):
        u.color = 'gray'
        path.append(u)
        if n < limit:
            nbrList = list(u.get_connections())
            i = 0
            done = False
            while i < len(nbrList) and not done:
                if nbrList[i].color == 'white':
                    done = knightTour(n+1, path, nbrList[i], limit)
                i = i + 1
            if not done:  # prepare to backtrack
                path.pop()
                u.color = 'white'
        else:
            done = True
        return done

def knights_tour(depth, path, u, limit):
    path.append(u)
    u.color = 'grey'
    if depth >= limit: #we found the path of required length
        return path
    
    

    connections = u.get_connections()
    for connection in connections:
        if connection.color == 'white':
            tour = knights_tour(depth+1,path, connection, limit)
            if tour: #a valid path was returned
                return tour
            else:
                #a valid path was not returned, backtrack
                path.pop()
                u.color = 'white'

    return False #no valid path exists

g = gen_knight_graph(4)
print(knights_tour(0,[],g[0], 14))
g = gen_knight_graph(4)
print(knightTour(0,[],g[0], 14))


g = Graph()
g.add_edge('A', 'D')
g.add_edge('A', 'B')
g.add_edge('B', 'D')
g.add_edge('B', 'C')
g.add_edge('D', 'E')
g.add_edge('E', 'B')
g.add_edge('E', 'F')
g.add_edge('F', 'C')
#print(knights_tour(0,[],g['A'], 5))
#print(knightTour(0,[],g['A'], 5))
#print(dfs(g,g['A']))

#Right answer is [A,B,D,E,F,C]
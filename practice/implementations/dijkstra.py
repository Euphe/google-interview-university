
class Vertex:

    def __init__(self, key, connections = None):
        self.key = key
        self.connections = connections or {}
        self.color = 'white'
        self.preceedor=None
        self.dist = 0

    def add_edge(self, vertex, weight=0):
        self.connections[vertex] = weight

    def get_connections(self):
        return self.connections.keys()

    def __gt__(self, other):
        return self.dist > other.dist
    def __repr__(self):
        return str(self.key)#+'(black), '+ ' connected to ' + str(['{}({})'.format(v.key, v.color) for v in self.get_connections()])

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

class MinHeap:
    #Heap order: given node x, parent p, x >= p

    def __init__(self):
        self._list = [0]

    def put(self, x):
        #First append the item to the list
        index = len(self._list)
        self._list.append(x)

        #Then swap item with parent until the heap order property is valid
        while index//2 > 0:
            parent = self._list[int(index/2)]
            if self._list[index] < parent:
                #swap
                temp = self._list[int(index/2)]
                self._list[int(index/2)] = self._list[index]
                self._list[index] = temp
            
            else:
                break
            index = int(index/2)

    def find_min(self):
        if len(self._list) > 1:
            return self._list[1]

    def min_child(self, i):
        if i*2+1 > len(self._list)-1:
            return i*2
        else:
            if self._list[i*2+1] > self._list[i*2]:
                return i*2
            else:
                return i*2+1

    def pop(self):
        
        if len(self._list) > 1:
            root = self._list[1] #Get the root of the tree
            #Put the last element of the tree in root's place
            self._list[1] = self._list[-1]
            del self._list[-1]
            #Swap the root with the smallest children until the heap order property is valid
            index = 1
            while index * 2 < len(self._list):
                
                min_child = self.min_child(index)

                if self._list[index] > self._list[min_child]:
                    temp = self._list[min_child]
                    self._list[min_child] = self._list[index]
                    self._list[index] = temp
                    index = min_child
                else:
                    break

            return root

    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        return len(self._list) - 1

    def _from_list(self, alist):
        
        self._list = [0] + alist[:]

        i = len(alist) // 2 #start in the middle of the list
        while (i > 0):
            #push the ith element as far down as it can go
            index = i
            while index * 2 < len(self._list):
                min_child = self.min_child(index)

                if self._list[index] > self._list[min_child]:
                    temp = self._list[min_child]
                    self._list[min_child] = self._list[index]
                    self._list[index] = temp
                    index = min_child
                else:
                    break

            i = i - 1

def dijkstra(g, start):
    INF = 99999
    start.dist = 0
    start.preceedor = None
    for vertex in g:
        if vertex != start:
            vertex.dist = INF #set current cost to getting to vertex

    process_queue = MinHeap() #priority queue, sorted by distance. Smaller distance first
    process_queue.put(start)
    while not process_queue.is_empty():
        #find node with smallest cost
        node = process_queue.pop()
        connections = node.get_connections()
        for connection in connections:
            new_dist = node.dist + node.connections[connection]
            if new_dist < connection.dist:
                connection.dist = new_dist
                connection.preceedor = node
                process_queue.put(connection)

g = Graph()
g.add_edge('1', '2', 1)
g.add_edge('2', '4', 10)
g.add_edge('1', '3', 2)
g.add_edge('3', '4', 5)

dijkstra(g, g['1'])




class Vertex:

    def __init__(self, key, connections = None):
        self.key = key
        self.connections = connections or {}
        self.color = 'white'
        self.preceedor=None
        self.discovery = 0
        self.finish = 0

    def add_edge(self, vertex, weight=0):
        self.connections[vertex] = weight

    def get_connections(self):
        return self.connections.keys()


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

class DFSGraph(Graph):
    def __init__(self, vertexes=None):
        super().__init__(vertexes)
        self.time = 0

    def dfs(self):
        for vertex in self:
            vertex.color = 'white'
            vertex.preceedor = None
        for vertex in self:
            if vertex.color == 'white':
                self.dfs_visit(vertex)


    def dfs_visit(self, start_vertex):
        start_vertex.color = 'grey'
        self.time += 1
        start_vertex.discovery = self.time
        for vertex in sorted(start_vertex.get_connections(), key=lambda v: v.key):
            if vertex.color == 'white':
                vertex.preceedor = start_vertex
                self.dfs_visit(vertex)
        start_vertex.color = 'black'
        self.time += 1
        start_vertex.finish = self.time

    def get_tree(self):
        vertexes = sorted(self.vertexes.values(), reverse=True, key=lambda v: v.discovery)
        return vertexes

g = DFSGraph()
g.add_edge('A', 'D')
g.add_edge('A', 'B')
g.add_edge('B', 'D')
g.add_edge('B', 'C')
g.add_edge('D', 'E')
g.add_edge('E', 'B')
g.add_edge('E', 'F')
g.add_edge('F', 'C')
g.dfs()
print(g)

tree = g.get_tree()
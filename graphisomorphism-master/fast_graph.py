
class FastVertex:
    def __init__(self, graph: "FastGraph", label):
        self._graph = graph
        self.label = label
        self._neighbours = list()

        self.colorClass = None
        self.colornum = 0
        self.newClassID = 0

    @property
    def neighbours(self):
        return self._neighbours

    @property
    def degree(self):
        return len(self._neighbours)

    def AddNeighbour(self, vertex: "FastVertex"):
        self._neighbours.append(vertex)

class FastGraph:
    def __init__(self, n: int):
        self._vertices = list()
        self._edges = list()

        for i in range(n):
            self._vertices.append(FastVertex(self, i))

    def Copy(self):
        copy = FastGraph(len(self._vertices))
        for edge in self._edges:
            copy.AddEdge(edge[0], edge[1])
        return copy

    def __contains__(self, vertex: "FastVertex"):
        return vertex._graph == self

    def __iter__(self):
        return iter(self._vertices)

    @property
    def vertices(self):
        return self._vertices
    
    @property
    def edges(self):
        return self._edges

    def AddEdge(self, v1: int, v2: int):
        vertex1 = self._vertices[v1]
        vertex2 = self._vertices[v2]

        vertex1.AddNeighbour(vertex2)
        vertex2.AddNeighbour(vertex1)

        self._edges.append((v1, v2))
    
        
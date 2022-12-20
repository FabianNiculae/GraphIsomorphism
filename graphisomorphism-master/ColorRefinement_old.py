
import graph as g
import graph_io as gio

from RollingSieve import RollingSieve

class NaiveColorGen:
    def __init__(self, start):
        self.__n = start - 1
    
    def Next(self):
        self.__n += 1
        return self.__n

def ColorRefine(vertices, init_colors=True):

    if init_colors:                         # Initialize the uniform coloring
        for vertex in vertices:
            vertex.colornum = 2             # We use prime number coloring and 2 is the first
    
    while ColorRefineIteration(vertices):   # Iteratively update the coloring
        pass
    
def ColorRefineIteration(vertices):

    for v in vertices:          
        v.newcolor = 2          # Initialize the new coloring
        v.colordups = 1         # Keep track of color duplicates

    # colorGen = NaiveColorGen(3)
    colorGen = RollingSieve()   # Use a incremental prime sieve to generate the colors

    for i in range(len(vertices) - 1):
        for j in range(i+1, len(vertices)):
            v1 = vertices[i]
            v2 = vertices[j]

            if v1.colornum == v2.colornum:
                if SameNeighbourhood(v1, v2):       # Same color and same neighbourhood
                    v2.newcolor = v1.newcolor       
                    v1.colordups += 1               # Keep track of color duplicates
                    v2.colordups += 1

                elif v2.newcolor == v1.newcolor:    # Same color and different neighbourhood
                    v2.newcolor = colorGen.Next()   

            elif v2.newcolor == v1.newcolor:        # Different color
                v2.newcolor = colorGen.Next()       

    updated = False
    for v in vertices:          
        updated |= v.colornum != v.newcolor         # Check if the coloring has changed
        v.colornum = v.newcolor                     # Assign the new coloring

    return updated

def SameNeighbourhood(vertex1, vertex2):   
    return ColorProd(vertex1.neighbours) == ColorProd(vertex2.neighbours)

    # if vertex1.degree != vertex2.degree:
    #     return False

    # n1 = sorted(vertex1.neighbours, key=lambda v: v.colornum)
    # n2 = sorted(vertex2.neighbours, key=lambda v: v.colornum)
    # for i in range(len(n1)):
    #     if n1[i].colornum != n2[i].colornum:
    #         return False
    # return True

def ColorProd(vertices):
    prod = 1
    for n in vertices:
        prod *= n.colornum
    return prod

if __name__ == "__main__":

    import time

    colorGen = RollingSieve()

    # tests = "cref9vert_4_9"
    tests = "colorref_largeexample_4_1026"
    # tests = "cubes3"

    with open("SampleGraphsSet1/{}.grl".format(tests), 'r') as gl:
        graphList = gio.load_graph(gl, read_list=True)[0]

    for i in range(len(graphList) - 1):
        for j in range(i+1, len(graphList)):

            graph = graphList[i] + graphList[j] 

            t =time.time()
            ColorRefine(graph.vertices)
            print(time.time() - t)

        # with open("{}_result{}{}{}.dot".format(tests, "comb", i, j), 'w') as out:
        #     gio.write_dot(graph, out)


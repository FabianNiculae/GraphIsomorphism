import fast_graph as fg
import fast_graph_io as fgio

from FastColorRefinement import ColorRefine
import ColorClass

import time

times = []

def IsIsomorphic(graph1, graph2):
    pass

def CountIsomorphisms(graph1, graph2):
    
    if len(graph1.vertices) != len(graph2.vertices):
        return 0
    
    vertexUnion = graph1.vertices + graph2.vertices
    return CountIsomorphismsRecursive(graph1, graph2, vertexUnion, [], [])


def CountAutomorphisms(graph):
    graphCopy = graph.Copy()
    vertexUnion = graph.vertices + graphCopy.vertices
    return CountIsomorphismsRecursive(graph, graphCopy, vertexUnion, [], [])


def CountIsomorphismsRecursive(graph1, graph2, vertexUnion, D, I):

    partition = [ColorClass.GetFirst()]

    for vertex in vertexUnion:
        vertex.colornum = 0

    for x, y in zip(D, I):
        partition[-1].AddVertex(x)
        partition[-1].AddVertex(y)
        partition.append(ColorClass.GetNext())
    
    for vertex in vertexUnion:
        if vertex.colornum == 0:
            partition[-1].AddVertex(vertex)

    ColorRefine(partition)

    if not BalancedColoring(graph1, graph2):
        return 0

    x = FindDuplicateColor(graph1)
    # x = FindBiggestDuplicateColor(graph1, partition) # Not Faster.
    if x is None:
        return 1
    
    dups_graph2 = [vertex for vertex in x.colorClass if vertex in graph2]
    num = 0    
    for y in dups_graph2:
        D.append(x), I.append(y)
        num += CountIsomorphismsRecursive(graph1, graph2, vertexUnion, D, I)
        D.pop(), I.pop()
    
    return num

def BalancedColoring(graph1, graph2):
    return ColorProd(graph1.vertices) == ColorProd(graph2.vertices)

def ColorProd(vertices):
    prod = 1
    for vertex in vertices:
        prod *= vertex.colornum
    return prod

def FindDuplicateColor(graph):
    for vertex in graph:
        if vertex.colorClass.Size() > 2:
            return vertex
    return None

# Branch on the biggest color class -> Not faster than first duplicate.
def FindBiggestDuplicateColor(graph, partition):
    biggest = None
    for colorClass in partition:
        try:
            if colorClass.Size() > biggest.Size():
                biggest = colorClass
        except AttributeError:
            if colorClass.Size() > 2:
                biggest = colorClass
    
    if biggest is None:
        return None
    
    for vertex in colorClass:
        if vertex in graph:
            return vertex


if __name__ == "__main__":
    
    import time

    # tests = "cref9vert_4_9"
    # tests = "colorref_largeexample_4_1026"
    tests = "products72"

    with open("SampleGraphsSet1/{}.grl".format(tests), 'r') as gl:
        graphList = fgio.load_graph(gl, read_list=True)

    for graph in graphList:
        t = time.time()
        print("# of automorphisms: {}".format(CountAutomorphisms(graph)))
        print("Time to compute: {}".format(time.time() - t))
        print()


    # for i in range(len(graphList) - 1):
    #     for j in range(i+1, len(graphList)):
            
    #         graph1 = graphList[i]
    #         graph2 = graphList[j]

    #         t = time.time()
    #         result = CountIsomorphisms(graph1, graph2)
    #         print("# of isomorphisms [{}, {}]: {}".format(i, j, result))
    #         print("Time to compute: {}".format(time.time() - t))
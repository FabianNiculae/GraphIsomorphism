import graph_io as gio

from ColorRefinement_old import ColorRefine
from ColorRefinement_old import ColorProd
from RollingSieve import RollingSieve

# iteration = -1
# success = 1

def CountIsomorphisms(graph1, graph2):

    vertices1 = graph1.vertices
    vertices2 = graph2.vertices
    union = vertices1 + vertices2         # Create a union in advance to avoid unnecessary copying

    if len(vertices1) != len(vertices2):  # Graphs with different vertex amounts can't be isomorphic
        return 0

    return CountIsomorphismsRecursive(vertices1, vertices2, union, [], [])

def CountIsomorphismsRecursive(vertices1, vertices2, union, D, I):

    for v in union:
        v.colornum = 2                  # Initialize the uniform coloring
    
    colorGen = RollingSieve()
    for i in range(len(D)):             # Create the initial coloring based on D and I
        next_color = colorGen.Next()
        D[i].colornum = next_color
        I[i].colornum = next_color   

    ColorRefine(union, False)           # Create the coloring induced by D and I 

    # global iteration, success
    # iteration += 1

    if not BalancedColoring(vertices1, vertices2):
        # print("Fail: ", iteration)
        return 0
    
    x = FindDuplicateColor(vertices1)
    if x is None:       # A balanced coloring without duplicates implies a bijection
        # print("Succes: ", iteration, "#", success)
        # success += 1
        return 1

    num = 0

    dups2 = [v for v in vertices2 if v.colornum == x.colornum]
    for y in dups2:     # Loop over all duplicates in vertices2 that match x
        D.append(x), I.append(y)
        num += CountIsomorphismsRecursive(vertices1, vertices2, union, D, I)
        D.pop(), I.pop()                # Avoid contaminating the next iteration
    
    return num



def BalancedColoring(vertices1, vertices2):
    return ColorProd(vertices1) == ColorProd(vertices2)
    # for v in vertices:
    #     if v.colordups % 2 == 1:
    #         return False
    # return True

def FindDuplicateColor(vertices):
    for v in vertices:
        if v.colordups > 2:     # Vertices should have a balanced coloring, so every color has
            return v            # at least one duplicate by definition, hence v.colordups > 2
    return None

if __name__ == "__main__":
    
    import time

    # tests = "cref9vert_4_9"
    tests = "colorref_largeexample_4_1026"
    # tests = "cubes3"

    with open("SampleGraphsSet1/{}.grl".format(tests), 'r') as gl:
        graphList = gio.load_graph(gl, read_list=True)[0]
    
    for i in range(len(graphList) - 1):
        for j in range(i+1, len(graphList)):
            
            graph1 = graphList[i]
            graph2 = graphList[j]

            graph = graph1 + graph2

            t = time.time()
            result = CountIsomorphisms(graph1, graph2)
            print("# of isomorphisms [{}, {}]: {}".format(i, j, result))
            print("Time to compute: {}".format(time.time() - t))     
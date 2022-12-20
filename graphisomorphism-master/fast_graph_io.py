import sys
from typing import IO, Tuple, List, Union

from fast_graph import FastGraph

DEFAULT_COLOR_SCHEME = "paired12"
NUM_COLORS = 12


def read_line(f: IO[str]) -> str:
    """
    Read a single non-comment line from a file
    :param f: The file
    :return: the line
    """
    line = f.readline()

    while len(line) > 0 and line[0] == '#':
        line = f.readline()

    return line

def read_graph(f: IO[str]) -> Tuple[FastGraph, List[str], bool]:
    """
    Read a graph from a file
    :param f: The file
    :return: The graph
    """

    numVertices = int(read_line(f))
    graph = FastGraph(numVertices)

    line = read_line(f)
    while len(line) > 0 and line[0] != '-':
        comma = line.find(',')
        graph.AddEdge(int(line[:comma]), int(line[comma+1:]))
        line = read_line(f)

    return graph, len(line) > 0

def read_graph_list(f: IO[str]) -> List[FastGraph]:
    """
    Read a list of graphs from a file
    :param f: The file
    :return: A list of graphs
    """

    graphs = list()
    more_graphs = True

    while more_graphs:
        graph, more_graphs = read_graph(f)
        graphs.append(graph)

    return graphs

def load_graph(f: IO[str], read_list: bool = False) -> Union[List[FastGraph], FastGraph]:
    """
    Load a graph from a file
    :param f: The file
    :param read_list: Specifies whether to read a list of graphs from the file, or just a single graph.
    :return: The graph, or a list of graphs.
    """

    if read_list:
        return read_graph_list(f)
    return read_graph(f)

def write_dot(graph: FastGraph, f: IO[str]):
    """
    Writes a given graph to a file in .dot format.
    :param graph: The graph including vertex labels and coloring.
    :param f: The file.
    """

    f.write("graph G {\n")
    
    colors = dict()
    nextColor = 0

    for v in graph.vertices:
        if v.colornum not in colors.keys():
            colors[v.colornum] = nextColor
            nextColor += 1

        color = colors[v.colornum]

        options = 'penwidth=3,label="{}",color={},colorsheme={}'    \
                    .format(v.label, color % NUM_COLORS + 1, DEFAULT_COLOR_SCHEME)
        if color > NUM_COLORS:
            options += ',style=filled,fillcolor={}'.format((color // NUM_COLORS) % NUM_COLORS + 1)
    
        f.write('    {} [{}]\n'.format(v.label, options))
    
    f.write('\n')
    for e in graph.edges:
        f.write('    {}--{}\n'.format(e[0], e[1]))

    f.write('}\n')



if __name__ == "__main__":

    with open("SampleGraphsSet1/cref9vert_4_9.grl", 'r') as g:
        graph = load_graph(g, read_list=True)[0]

    for v in graph.vertices:
        print(v.neighbours)

    with open("DOT_OUT/io_test", 'w') as dot:
        write_dot(graph, dot)
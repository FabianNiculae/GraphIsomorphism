
import fast_graph as fg
import fast_graph_io as fgio

from Queue import Queue
import ColorClass

def ColorRefine(partition):

    refinementQueue = Queue()
        
    for colorClass in partition:                # Add all colorclasses that don't have the default color.
        if colorClass.color != 2:
            refinementQueue.Append(colorClass)
    
    if len(refinementQueue) == 0:               # If the queue is still empty, add the default colorclass.
        refinementQueue.Append(partition[0])

    while len(refinementQueue) > 0:             # Keep refining until the queue is empty
        ColorRefineIteration(partition, refinementQueue)

def ColorRefineIteration(partition, refinementQueue):
    
    currentColorClass = refinementQueue.Pop()
    
    # List to keep track of color classes that might need to split.
    tentativeColorClasses = list()

    for vertex in currentColorClass:          
        for neighbour in vertex.neighbours:     
            # Set newClassID as the number of edges into the current color class.
            neighbour.newClassID += 1

            colorClass = neighbour.colorClass
            if not colorClass.tentative:
                # Add the color class to the tentative list.
                tentativeColorClasses.append(colorClass)
                colorClass.tentative = True

    # Split every color class in the tentative list based on the newClassID.
    for colorClass in tentativeColorClasses:
    
        newColorClasses = colorClass.Split()

        # Add the smallest color classes to the queue.
        biggestColorClass = colorClass
        for newColorClass in newColorClasses:

            partition.append(newColorClass)
            
            if colorClass.inQueue or newColorClass.Size() < biggestColorClass.Size():
                refinementQueue.Append(newColorClass)
            
            else:
                refinementQueue.Append(biggestColorClass)
                biggestColorClass = newColorClass

        colorClass.tentative = False

if __name__ == "__main__":

    tests = ["cref9vert_4_9.grl"]

    for test in tests:
        
        with open("SampleGraphsSet1/{}".format(test), 'r') as gl:
            graphs = fgio.load_graphs(gl, read_list=True)
        
        for i in range(len(graphs)):
            partition = [ColorClass.GetFirst()]
            for vertex in graphs[i].vertices:
                partition[0].AddVertex(vertex)
            ColorRefine(partition)
        
            with open("DOT_OUT/{}_result{}.dot".format(test, i), 'w') as dot:
                fgio.write_dot(graphs[i], dot)

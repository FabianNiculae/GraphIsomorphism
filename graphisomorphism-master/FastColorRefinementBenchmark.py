
import graph as g
import graph_io as gio

from Queue import Queue
import ColorClass
import ColorClass_old

times = []

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
    
    global times

    currentColorClass = refinementQueue.Pop()
    
    # List to keep track of color classes that might need to split.
    tentativeColorClasses = list()

    t = time.time();

    for vertex in currentColorClass:          
        for neighbour in vertex.neighbours:     
            # Set newClassID as the number of edges into the current color class.
            try:
                neighbour.newClassID += 1
            except AttributeError:
                neighbour.newClassID = 1

            colorClass = neighbour.colorClass
            if not colorClass.tentative:
                # Add the color class to the tentative list.
                tentativeColorClasses.append(colorClass)
                colorClass.tentative = True

    times[0] += (time.time() - t)

    # Split every color class in the tentative list based on the newClassID.
    for colorClass in tentativeColorClasses:
        
        t = time.time();

        # newColorClasses = dict()
        # originalColorClassID = colorClass.vertices.First().newClassID

        # for vertex in colorClass:
        #     if vertex.newClassID != originalColorClassID:
        #         vertex.colorClass.RemoveVertex(vertex)
        #         try:
        #             newColorClasses[vertex.newClassID].AddVertex(vertex)
        #         except KeyError:
        #             newColorClasses[vertex.newClassID] = ColorClass.GetNext()
        #             newColorClasses[vertex.newClassID].AddVertex(vertex)
            
        #     vertex.newClassID = 0

        newColorClasses = colorClass.Split()

        times[1] += (time.time() - t)

        t = time.time();

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

        times[2] += (time.time() - t)

def ColorRefine2(partition):

    refinementQueue = Queue()
        
    for colorClass in partition:                # Add all colorclasses that don't have the default color.
        if colorClass.color != 2:
            refinementQueue.Append(colorClass)
    
    if len(refinementQueue) == 0:               # If the queue is still empty, add the default colorclass.
        refinementQueue.Append(partition[0])

    while len(refinementQueue) > 0:             # Keep refining until the queue is empty
        ColorRefineIteration2(partition, refinementQueue)

def ColorRefineIteration2(partition, refinementQueue):
    
    global times

    currentColorClass = refinementQueue.Pop()
    
    # List to keep track of color classes that might need to split.
    tentativeColorClasses = list()

    t = time.time();

    for vertex in currentColorClass:          
        for neighbour in vertex.neighbours:     
            # Set newClassID as the number of edges into the current color class.
            try:
                neighbour.newClassID += 1
            except AttributeError:
                neighbour.newClassID = 1

            colorClass = neighbour.colorClass
            if not colorClass.tentative:
                # Add the color class to the tentative list.
                tentativeColorClasses.append(colorClass)
                colorClass.tentative = True

    times[0] += (time.time() - t)

    # Split every color class in the tentative list based on the newClassID.
    for colorClass in tentativeColorClasses:
        
        t = time.time();

        newColorClasses = dict()
        originalColorClassID = colorClass.vertices.First().newClassID

        for vertex in colorClass:
            if vertex.newClassID != originalColorClassID:
                vertex.colorClass.RemoveVertex(vertex)
                try:
                    newColorClasses[vertex.newClassID].AddVertex(vertex)
                except KeyError:
                    newColorClasses[vertex.newClassID] = ColorClass_old.GetNext()
                    newColorClasses[vertex.newClassID].AddVertex(vertex)
            
            vertex.newClassID = 0

        # newColorClasses = colorClass.Split()

        times[1] += (time.time() - t)

        t = time.time();

        # Add the smallest color classes to the queue.
        biggestColorClass = colorClass
        for newColorClass in newColorClasses.values():
            partition.append(newColorClass)
            
            if colorClass.inQueue or newColorClass.Size() < biggestColorClass.Size():
                refinementQueue.Append(newColorClass)
            
            else:
                refinementQueue.Append(biggestColorClass)
                biggestColorClass = newColorClass

        colorClass.tentative = False

        times[2] += (time.time() - t)




if __name__ == "__main__":
    
    import time

    tests = ["threepaths160", "threepaths320", "threepaths640", "threepaths1280"]

    for test in tests:

        print("Benchmark {}:".format(test))
        
        with open("SampleGraphsSet1/{}.gr".format(test), 'r') as g:
            graph = gio.load_graph(g)

        for i in range(4):
            times = [0, 0, 0]

            partition = [ColorClass_old.GetFirst()]
            for vertex in graph.vertices:
                partition[0].AddVertex(vertex)              
            ColorRefine2(partition)

            total = times[0] + times[1] + times[2]
            print("\tOld: total:{}\t{}".format(total, times))

        print()

        for i in range(4):
            times = [0, 0, 0]

            partition = [ColorClass.GetFirst()]
            for vertex in graph.vertices:
                partition[0].AddVertex(vertex)              
            ColorRefine(partition)

            total = times[0] + times[1] + times[2]
            print("\tNew: total:{}\t{}".format(total, times))

    exit()












    # tests = "cref9vert_4_9"
    tests = "colorref_largeexample_4_1026"
    # tests = "cubes3"

    with open("SampleGraphsSet1/{}.grl".format(tests), 'r') as gl:
        graphList = gio.load_graph(gl, read_list=True)[0]

    for i in range(len(graphList) - 1):
        for j in range(i+1, len(graphList)):

            graph = graphList[i] + graphList[j]
        
            start = time.time()

            partition = [ColorClass.GetFirst()]
            for vertex in graph.vertices:
                partition[0].AddVertex(vertex)              
            ColorRefine(partition)

            print(time.time() - start)

        # with open("DOT_OUT/{}_{}_result.dot".format(tests, i), 'w') as out:
            # gio.write_dot(graphList[i], out)

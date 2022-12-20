
# from DoublyLinkedList import DoublyLinkedList
from RollingSieve import RollingSieve

class ColorClass:
    def __init__(self, color):
        self._vertices = list()
        self._color = color
        self.inQueue = False
        self.tentative = False

    @property
    def vertices(self):
        return self._vertices
    
    @property
    def color(self):
        return self._color

    def AddVertex(self, vertex):
        vertex.colorClass = self
        vertex.colornum = self._color
        self._vertices.append(vertex)
    
    def Split(self):
        originalClass = list()
        originalColorClassID = self._vertices[0].newClassID

        newColorClasses = dict()

        for vertex in self._vertices:
            if vertex.newClassID != originalColorClassID:
                try:
                    newColorClasses[vertex.newClassID].AddVertex(vertex)
                except KeyError:
                    newColorClasses[vertex.newClassID] = GetNext()
                    newColorClasses[vertex.newClassID].AddVertex(vertex)
            else:
                originalClass.append(vertex)
            
            vertex.newClassID = 0
        
        self._vertices = originalClass

        return newColorClasses.values()
        

    def __iter__(self):
        return iter(self._vertices)
    
    def Size(self):
        return len(self._vertices)

    def __str__(self):
        return "ColorClass: {}".format(self._color)
    
    def __repr__(self):
        return str(self)
        

_colorGen = RollingSieve()

def GetNext():
    global _colorGen
    return ColorClass(_colorGen.Next())

def GetFirst():
    global _colorGen
    _colorGen = RollingSieve()
    return ColorClass(2)
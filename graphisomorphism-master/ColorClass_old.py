
from DoublyLinkedList import DoublyLinkedList
from RollingSieve import RollingSieve

class ColorClass:
    def __init__(self, color):
        self.__vertices = DoublyLinkedList()
        self.__color = color
        self.inQueue = False
        self.tentative = False

    @property
    def vertices(self):
        return self.__vertices
    
    @property
    def color(self):
        return self.__color

    def AddVertex(self, vertex):
        vertex.colorClass = self
        vertex.colornum = self.__color
        self.__vertices.Append(vertex)
    
    def RemoveVertex(self, vertex):
        self.__vertices.Remove(vertex)

    def __iter__(self):
        return iter(self.__vertices)
    
    def Size(self):
        return len(self.__vertices)

    def __str__(self):
        return "ColorClass: {}".format(self.__color)
    
    def __repr__(self):
        return str(self)
        

__colorGen = RollingSieve()

def GetNext():
    global __colorGen
    return ColorClass(__colorGen.Next())

def GetFirst():
    global __colorGen
    __colorGen = RollingSieve()
    return ColorClass(2)
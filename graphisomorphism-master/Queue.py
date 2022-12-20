
class Item:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    def Next(self):
        return self.__next
    
    def SetNext(self, item):
        self.__next = item
    
    @property
    def data(self):
        return self.__data

class Queue():
    def __init__(self):
        self.__first = None
        self.__last = None
        self.__size = 0
    
    def Append(self, data):
        new_item = Item(data)
        if self.__size == 0:
            self.__first = new_item
            self.__last = self.__first
        else:
            self.__last.SetNext(new_item)
            self.__last = self.__last.Next()
        
        self.__size += 1
        data.inQueue = True
    
    def Pop(self):
        assert self.__size > 0
        result = self.__first.data
        self.__first = self.__first.Next()
        self.__size -= 1
        result.inQueue = False
        return result

    def __str__(self):
        s = '[' + str(self.__first.data)
        i = self.__first.Next()
        while i is not None:
            s += ', ' + str(i.data)
            i = i.Next()
        s += ']'
        return s

    def __len__(self):
        return self.__size
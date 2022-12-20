
class Item:
    def __init__(self, data, parent):
        self.__data = data
        self.__prev = None
        self.__next = None
        self.__parent = parent
    
    def SetPrev(self, item):
        self.__prev = item

    def Prev(self):
        return self.__prev

    def SetNext(self, item):
        self.__next = item

    def Next(self):
        return self.__next

    @property
    def data(self):
        return self.__data
    
    @property
    def parent(self):
        return self.__parent
        

class DoublyLinkedList:
    def __init__(self):
        self.__first = None
        self.__last = None
        self.__size = 0
    
    def Append(self, data):
        new_item = Item(data, self)
        if self.__size == 0:
            self.__first = new_item
            self.__last = self.__first
        else:
            last = self.__last
            self.__last.SetNext(new_item)
            self.__last = self.__last.Next()
            self.__last.SetPrev(last)
        self.__size += 1
        data.item = self.__last

    def Remove(self, data):
        item = data.item

        if item == self.__first:
            self.__first = self.__first.Next()
            self.__first.SetPrev(None)
        elif item == self.__last:
            self.__last = self.__last.Prev()
            self.__last.SetNext(None)
        else:
            item.Prev().SetNext(item.Next())
            item.Next().SetPrev(item.Prev())

        self.__size -= 1
        data.item = None
    
    def First(self):
        return self.__first.data

    def __len__(self):
        return self.__size
    
    def __iter__(self):
        self.__i = self.__first
        return self
    
    def __next__(self):
        if self.__i is None:
            raise StopIteration
        result = self.__i
        self.__i = self.__i.Next()
        return result.data



if __name__ == "__main__":

    class TestObj:
        def __init__(self, value):
            self.__value = value

        def __str__(self):
            return str(self.__value) 


    dll = DoublyLinkedList()
    remove0 = None
    remove6 = None
    remove9 = None

    for i in range(10):       
        obj = TestObj(i)
        dll.Append(obj)
        if i == 0:
            remove0 = obj
        if i == 6:
            remove6 = obj
        if i == 9:
            remove9 = obj
    
    for data in dll:
        print(data)
    
    print()
    dll.Remove(remove0)
    dll.Remove(remove6)
    dll.Remove(remove9)

    for data in dll:
        print(data)
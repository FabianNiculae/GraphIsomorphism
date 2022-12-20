
class Item:
    def __init__(self, data):
        self.__item = data
        self.__next = None

    def Next(self):
        return self.__next
    
    def SetNext(self, item):
        self.__next = item
    
    @property
    def item(self):
        return self.__item

class LinkedList:
    def __init__(self, data = None):
        self.__first = None
        self.__last = None
        self.__size = 0

        if data is not None:
            for item in data:
                self.Append(item)
    
    def Append(self, data):
        new_item = Item(data)
        if self.__size == 0:
            self.__first = new_item
            self.__last = self.__first
        else:
            self.__last.SetNext(new_item)
            self.__last = self.__last.Next()
        
        self.__size += 1
    
    def __find(self, index):
        assert index >= 0 and index < self.__size

        item = self.__first
        for i in range(index):
            item = item.Next()
        
        return item

    def Remove(self, index):
        item = None
        
        if index == 0:
            item = self.__first
            self.first = item.Next()
        else:
            prev = self.__find(index - 1)
            item = prev.Next()
            prev.SetNext(item.Next())
        
        self.__size -= 1
        return item.item

    def get(self, index):
        return self.__find(index).item

    def __len__(self):
        return self.__size
    
    def __iter__(self) :
        self.__i = self.__first
        return self

    def __next__(self) :
        if self.__i == None :
            raise StopIteration
        result = self.__i
        self.__i = self.__i.Next()
        return result.item
        
if __name__ == "__main__":

    ll = LinkedList([-2, -1])

    for i in range(10):
        ll.Append(i)
    
    ll.Remove(3)

    for item in ll:
        print(item)

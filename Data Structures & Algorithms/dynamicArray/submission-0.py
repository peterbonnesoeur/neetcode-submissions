class DynamicArray:
    
    def __init__(self, capacity: int):
        self.array = []
        self.capacity = capacity

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n
        return

    def pushback(self, n: int) -> None:
        if self.getSize() == self.getCapacity():
            self.resize()
        self.array.append(n)

    def popback(self) -> int:

        return self.array.pop(-1)
 

    def resize(self) -> None:
        self.capacity = 2 * self.capacity


    def getSize(self) -> int:
        return len(self.array)
        
    
    def getCapacity(self) -> int:
        return self.capacity

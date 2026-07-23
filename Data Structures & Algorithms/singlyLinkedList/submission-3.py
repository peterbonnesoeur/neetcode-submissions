class LinkedList:
    
    def __init__(self):
        self.array = []
        return
    
    def get(self, index: int) -> int:
        if index >= len(self.array):
            return -1
        return self.array[index]

    def insertHead(self, val: int) -> None:
        self.array = [val] + self.array
        return

    def insertTail(self, val: int) -> None:
        self.array.append(val)
        return
        

    def remove(self, index: int) -> bool:
        if index < len(self.array):
            self.array.pop(index)
            return True
        else:
            return False
        

    def getValues(self) -> List[int]:
        return self.array

class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.val = value
        self.next = None


class HashTable:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.array = [None] * capacity
        self.size = 0

    def hash_function(self, key: int) -> int:
        return key % self.capacity

    def insert(self, key: int, value: int) -> None:
        
        index = self.hash_function(key)
        node = self.array[index]
        while self.array[index] is not None and index < len(self.array) :
            index += 1
        
        if not node:
            self.array[index] = Node(key, value)
            self.size += 1
        else:
            prev = None
            while node:
                if node.key == key:
                    node.val = value
                    return
                else:
                    prev = node
                    node = node.next
            prev.next = Node(key, value)
            self.size+=1
        # Check if resizing is needed
        if self.size / self.capacity >= 0.5:
            self.resize()

    def get(self, key: int) -> int:
        index = self.hash_function(key)
        node = self.array[index]

        while node:
            if node.key == key:
                return node.val
            node = node.next

        return -1

    def remove(self, key: int) -> bool:
        index = self.hash_function(key)
        node = self.array[index]
        prev = None

        while node:
            if node.key == key:
                if prev:
                    prev.next = node.next
                else:
                    self.array[index] = node.next
                self.size -= 1
                return True
            prev, node = node, node.next

        return False

    def getSize(self) -> int:
        return self.size


    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        old_array = self.array.copy()
        self.capacity = 2*self.capacity
        self.array = [None]*self.capacity
        self.size = 0
        for item in old_array:
            if item is not None:
                node = item
                while node:
                    self.insert(node.key, node.val)
                    node = node.next


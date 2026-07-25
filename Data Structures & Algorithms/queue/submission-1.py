class Node:
    def __init__(self, val: int, next_node: Node = None, prev_node: Node = None):
        self.val = val
        self.next = next_node
        self.prev = prev_node


class Deque:
    
    def __init__(self):
        # Init a dummy node
        self.head = Node(-1)
        self.tail = self.head
        self.size = 0


    def isEmpty(self) -> bool:
        return self.size == 0
            

    def append(self, value: int) -> None:
        node = Node(value)
        if self.size == 0:
            node.prev = self.head
            self.head.next = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = self.tail.next

        self.size +=1        

    def appendleft(self, value: int) -> None:
        node = Node(value)
        if self.size == 0:
            node.prev = self.head
            self.head.next = node
            self.tail = node
        else:
            node.prev = self.head
            node.next = self.head.next
            # Don't w=forget to also change the the prev to point
            # to the new node, not head
            self.head.next.prev = node
            self.head.next = node
        
        self.size +=1
        

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        else:
            node = self.tail
            self.tail = self.tail.prev
            self.size -=1
            val = node.val
            del(node)
            return val
        

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        else:
            node = self.head.next
            self.head.next = node.next
            self.size -=1
            if self.size == 0:
                self.tail = self.head
            val = node.val
            del(node)
            return val
        

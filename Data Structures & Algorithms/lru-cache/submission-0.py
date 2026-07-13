class Node:
    def __init__(self, key: int, val: int):
        self.key = key # WE NEED THE KEYYY, otherwise, we can't remove it again...
        self.val = val
        self.next: Optional[Node] = None
        self.prev: Optional[Node] = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.memory = {}
        self.tail = None
        self.head = None

    def reorder(self, curr_node: Node) -> None:
        if curr_node == self.tail:
            return
        
        if curr_node.next is not None:
            curr_node.next.prev = curr_node.prev
        
        if curr_node.prev is not None:
            curr_node.prev.next = curr_node.next
        elif self.head == curr_node:
            self.head = curr_node.next

        if self.tail is not None:
            self.tail.next = curr_node
            curr_node.prev = self.tail
            curr_node.next = None
            self.tail = curr_node
        else:
            self.head = self.tail = curr_node

    def get(self, key: int) -> int:
        if key not in self.memory:
            return -1
        curr_node: Node = self.memory[key]
        self.reorder(curr_node)
        return curr_node.val

    def put(self, key: int, value: int) -> None:
        if key in self.memory:
            node: Node = self.memory[key]
            node.val = value
            self.reorder(node)
        else:
            node : Node = Node(key, value)
            self.memory[key] = node
            self.reorder(node)
            if len(self.memory) > self.capacity:
                if self.head:
                    del self.memory[self.head.key]
                    self.head = self.head.next
                    if self.head:
                        self.head.prev = None
                    else:
                        self.tail = None
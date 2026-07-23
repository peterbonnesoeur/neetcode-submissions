class ListNode:
    def __init__(self, val, next_node = None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
        self.size = 0
    
    def get(self, index: int) -> int:
        if index < self.size:
            # print(self.getValues())
            curr = self.head
            for _ in range(index):
                curr = curr.next
            return curr.next.val
        else:
            return -1

    def insertHead(self, val: int) -> None:
        newNode = ListNode(val, self.head.next)
        self.head.next = newNode
        if not newNode.next:  # If list was empty before insertion
            self.tail = newNode
        self.size +=1

    def insertTail(self, val: int) -> None:
        newNode = ListNode(val)
        self.tail.next = newNode
        self.tail = self.tail.next
        self.size +=1
        

    def remove(self, index: int) -> bool:
        if index < self.size:
            curr = self.head
            for _ in range(index):
                curr = curr.next

            node = curr.next
            curr.next = node.next
            if node.next == None:
                self.tail = curr
            del(node)
            self.size -= 1

            return True
        else:
            return False
        

    def getValues(self) -> List[int]:
        array = []
        curr = self.head.next
        while curr:
            array.append(curr.val)
            curr = curr.next
        return array

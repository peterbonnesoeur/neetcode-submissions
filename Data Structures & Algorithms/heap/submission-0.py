class MinHeap:
    """
        implementation of a heap system ( I am scared)
        The heap is a list where left is at index 2n and right at 2n+1

        It is a complete tree -> meaning that the last row of children is always populated
        from left to right
    """
    
    def __init__(self):
        self.heap = [0] # emulate a 1 index



    def push(self, val: int) -> None:
        """ Push a new element in the heap and bubble it up
        """
        self.heap.append(val)
        self._bubble_up(len(self.heap) - 1)
       

    def pop(self) -> int:
        """
            Pop the smallest element of the heap
            and bubble_down the lastly added element
            to keep our heap a min heap
        """
        
        if len(self.heap) <= 1:
            return -1
        if len(self.heap) == 2:
            return self.heap.pop()

        root = self.heap[1]
        self.heap[1] = self.heap.pop()
        self._bubble_down(1)
        return root
        

    def top(self) -> int:
        """ Peek intot he min value of our heap"""
        return self.heap[1] if len(self.heap) >= 2 else -1
        

    def heapify(self, nums: List[int]) -> None:
        """ Generate a new heap from an array """
        self.heap = [0] + nums
        for i in reversed(range(1, len(self.heap)//2 + 1)):
            self._bubble_down(i)

    
    def _bubble_up(self, index: int) -> None:
        print(index)
        parent = index//2
        while index > 1 and self.heap[parent] > self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            index = parent
            parent = index//2

    def _bubble_down(self, index: int) -> None:
        child = 2*index

        while child < len(self.heap):
            # Min heap dude...
            if child + 1 < len(self.heap) and self.heap[child] > self.heap[child + 1]:
                child +=1

            if self.heap[child] >= self.heap[index]:
                break

            self.heap[child], self.heap[index] = self.heap[index], self.heap[child]
            index = child
            child = 2*index # left child

        
from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        self.cap = size
        self.q = deque()
        self.sum = 0

    def next(self, val: int) -> float:
        if len(self.q) < self.cap:
            self.sum += val
        else:
            self.sum += val - self.q.popleft()
        
        self.q.append(val)
        return self.sum/len(self.q)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

class MovingAverage:

    def __init__(self, size: int):
        self.cap = size
        self.array = []
        self.sum = 0

    def next(self, val: int) -> float:
        if len(self.array) < self.cap:
            self.sum += val
        else:
            self.sum += val - self.array.pop(0)
        
        self.array.append(val)
        return self.sum/len(self.array)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

class SegmentTree:
    
    def __init__(self, nums: List[int]):
        self.nums = nums.copy()
        self.moving_sum = []
        curr_sum = 0
        for num in self.nums:
            curr_sum += num
            self.moving_sum.append(curr_sum)
    
    def update(self, index: int, val: int) -> None:
        self.nums[index] = val
        curr_sum = 0
        if index > 0:
            curr_sum = self.moving_sum[index-1]
        
        # print(self.moving_sum, self.nums, curr_sum)
        for i in range(index, len(self.nums)):
            # print(i, self.nums[i])
            curr_sum += self.nums[i]
            self.moving_sum[i] = curr_sum
        # print(self.moving_sum)
    
    def query(self, L: int, R: int) -> int:
        
        if L != 0:
            min_term = self.moving_sum[L-1]
        else:
            min_term  = 0
        
        return self.moving_sum[R] - min_term


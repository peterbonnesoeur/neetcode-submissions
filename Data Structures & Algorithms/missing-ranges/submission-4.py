class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:

        if len(nums) == 0:
            print("here")
            return [[lower, upper]]

        res = []
        i = 1
        if nums[0] > lower:
            res.append([lower, nums[0]-1])

        l, r= nums[0], nums[0]
        while i < len(nums):
            r = nums[i]
            if r <= l or l+1 == r:
                l = nums[i]                
            else:
                res.append([l+1, r-1])
                l = nums[i]
            i+=1
                
            
        if r < upper:
            res.append([r+1, upper])
        return res
from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
         Brute force: counter
         linear time -> appear more than n/2
         space of o(1)
        """
        n = len(nums)
        mem = defaultdict(int)
        max_count = 0
        max_index = None
        for i in range(n):
            mem[nums[i]] += 1
            if mem[nums[i]] > max_count:
                max_count = mem[nums[i]]
                max_index = nums[i]

            if max_count > n/2:
                return max_index
        
        return max_index

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        memory :set[int] = set()
        for i, num in enumerate(nums):
            if len(memory) > k:
                memory.remove(nums[i-k-1])

            if num in memory:
                return True

            memory.add(num)
        
        return False
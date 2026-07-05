class Solution:
    def findIntervalTuples(self, nums : List[int], minimum: int) -> List[Tuple(int)]:
        limits =  [i for i in range(len(nums)) if nums[i] == minimum]
        intervals = []
        current = 0
        for limit in limits:
            intervals.append((current, limit))
            current = limit + 1
        intervals.append((current, len(nums)))
        return intervals


    def minNumberOperations(self, target: List[int], current_min: int = 0) -> int:
        """ Numbers >=1
            Bubbles up. 
            We do the problem iteratively on each subarray.
            First, we find the minimum of the subarray, or minimums if it has the same value.

            Then, for each subarrays, we do 2 things:
            1 - we find the min, then we increment the difference by currentMin - oldMin
        """
        if len(target) == 0:
            return 0

        target_min = min(target)

        res = target_min - current_min 

        boundaries = self.findIntervalTuples(target, target_min)

        for bound in boundaries:
            res += self.minNumberOperations(target = target[bound[0]:bound[1]], current_min = target_min)
        
        return res


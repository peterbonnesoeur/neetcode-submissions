import heapq

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        """

        Brute force is an option
        BUT we would forget a lot of things that  

        l,r = 0, 0
        diff = abs(nums[l]- nums[r])
        if diff > limit:
            limit - nums[l] -> check for numbers >= that one
        else:

        [4 , -2 , 0, 3]

        I would think of 2 pointers and a min and max heap.|
        Why heaps? In case we have repeated characters.

        If l, r are member of this heap, we can pop them out and have something 
        """

        max_size = 0        
        minHeap = []
        maxHeap = []

        l = 0
        # [1, 2] lim = 2
        for r, num in enumerate(nums):
            heapq.heappush(maxHeap, (-num, r))
            heapq.heappush(minHeap, (num, r))

            while -maxHeap[0][0] - minHeap[0][0] > limit:
                l += 1      
                while maxHeap and maxHeap[0][1] < l:
                    heapq.heappop(maxHeap)
                while minHeap and minHeap[0][1] < l:
                    heapq.heappop(minHeap)
            
            max_size = max(max_size, r - l)

        return max_size + 1

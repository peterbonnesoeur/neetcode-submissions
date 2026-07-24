class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        """
            Compute the maximum sum of circular subarray.
            The next element of nums[i ] is nums[(i+1) % n]

            BUT the subarray may only include each element of the fixed buffer at most once

            This looks really similar to kadane's algorithm, the main complexity here
            Is the circular nature of the array. but that limitation makes it apparent.

            We can circle the array of length 2 * n (by appending nums to nums)
            Then, with our currSum, we can detect when its anchoring point started 
            (aka when we began to sum it up), and if it exceed n size wise, we can remove an element of it
        """

        anchor = 0
        currSum = 0
        maxSum = nums[0]

        for i, num in enumerate(nums + nums):
        
            if i - anchor >= len(nums):
                
                currSum -= nums[anchor%len(nums)]  
                anchor += 1
                while anchor < i and nums[anchor%len(nums)] < 0:
                    currSum -= nums[anchor%len(nums)]
                    anchor += 1

            if currSum <= 0:
                anchor = i
                currSum = 0

            currSum += num
            maxSum = max(currSum, maxSum)

        return maxSum

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
            Find the maximum subarray given an array of integers
            The integers can be positive or negative.

            length can be between 1 and 1000
            We can do a 2 pointer techniques to identify the interval of the max subarray
            -> O(n)
            brute force is O(n**2) (double loop iteration)

            We can be samrt and think that we should stop our subarray sum when it dips below 0
            As it will never bring the maxSum up.
        """

        currSum = 0
        maxSum = nums[0] # putting the first element there since we need to retrieve the non empty element

        for num in nums:
            currSum = max(num, currSum + num) # Our gate to "drop" the subarray that is negative
            maxSum = max(maxSum, currSum)

        return maxSum
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        """

            it is all about finding the pivot point.

            First, we go from the end of the array and try to get the largest subarray in increasing order.
            Once we break this increasing order, we found our pivot. ex: [ 1 2 3] -> the pivot is 2 or [ 1 4 3 2] this pivot is 1.

            then, we replace the pivot by the smaller element of our increasing array -> we swap them:

            nums[pivot], nums[-1] = nums[-1], nums[pivot]
                -> that looks like: [1 2 3] -> 3 2 1 and [1 4 3 2] -> [2 4 3 1]
                                     |
            but not,w the order is not the next lexicographical one, we need to revert the subarray [pivot+1:]

        """

        pivot = len(nums) - 2

        while pivot >= 0 and nums[pivot] >= nums[pivot + 1]:
            pivot -= 1


        if pivot >= 0:
            successor = len(nums) - 1
            while nums[pivot] >= nums[successor]:
                successor -= 1
            nums[successor], nums[pivot] = nums[pivot], nums[successor]
        
        nums[pivot+1:] = nums[pivot+1:][::-1]
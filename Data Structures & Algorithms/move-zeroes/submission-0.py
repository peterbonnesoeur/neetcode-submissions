class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        the goal is to put the zeroes at the end of the array. all the zeroes
        Without an external array -> we modify things in place.

        What we want to do -> minimise the amount of travel in the array
        We also want to return the elements in place -> so remembering the past 0s location 
        Might not help as we can have: [1, 0,0,1,2,0,5] tha mkaes it annoying
        """
        
        for i in range(len(nums)):
            if nums[i] == 0:
                for j in range(i, len(nums)):
                    if nums[j] != 0:
                        nums[i], nums[j] = nums[j], nums[i]
                        break
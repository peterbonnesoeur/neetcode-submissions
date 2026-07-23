class Solution:
    def helper(self, i: int, currComb: list[int], combs:list[int], nums: list[int], target: int) -> None:
        """
            Helper function to get all the combinations that can reach target
        """
        # We escape in case we reached the desired length
        
        sum_char = 0
        if currComb:
            sum_char = sum(currComb)

        if sum_char == target:
            combs.append(currComb.copy())
            return

        if i > len(nums) or sum_char > target:
            return
        
        # There, we restrain the possibility
        # As we don't want duplicates, we prevent duplicates
        # such as [1,5] and [5,1] -> this is the way
        for possibility in range(i, len(nums)):

            currComb.append(nums[possibility])
            self.helper(possibility, currComb, combs, nums, target)
            # no need for the dimensionality reduction at that stage
            currComb.pop()

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
            The goal here is to see if the combination can ever go to target.
            Given that the target is always positive and the elements are always positive,
            there should be a reasonable amount of possibilities.

            The key part here is that we can add several times the same character

            Our exclusion policy is thus: exclusion based: i>n
            if the sum is > target
        """

        combs = []
        self.helper(0, [], combs, nums, target)
        return combs
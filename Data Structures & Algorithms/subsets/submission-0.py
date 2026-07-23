class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """ 
            We want to generate all the combinations of unique integers
            The solution must not contain duplicates. 
            The range of nums[i] is narrow, such as the range of length

            It is a combination exercise, so this is 2 ^ N -> 2^10 is 1000 combinations.
        """

        subsets : list[int]= []

        def helper(nums: list[int], curr_set: list[int], depth: int) -> None:
            if depth >= len(nums):
                subsets.append(curr_set.copy())
                return

            # We first do the case where we consider the current element
            curr_set.append(nums[depth])
            helper(nums, curr_set, depth+1)
            # Then, we do the case where we don't consider it
            curr_set.pop()
            helper(nums, curr_set, depth+1)

        helper(nums, [], 0)
        return subsets
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """ 
            We want to generate all the combinations of unique integers
            The solution must not contain duplicates. 
            The range of nums[i] is narrow, such as the range of length

            It is a combination exercise, so this is 2 ^ N -> 2^10 is 1000 combinations.

            The main issue here is that we don't want duplicates...
            So 1, 2_b, 2_a and 1,2_a,2_b are not allowed (in case of an array [1, 2_a, 2_b])

            Since the runtime is 2^n, we can safely 
        """

        subsets : list[int]= []

        #step 1 - We sort the array -> so that the duplicates are next to one another
        nums.sort()

        def helper(nums: list[int], curr_set: list[int], depth: int) -> None:
            if depth >= len(nums):
                subsets.append(curr_set.copy())
                # always think about returning/continue/pass
                return

            # We first do the case where we consider the current element
            # Here, we will compose with all the versions
            curr_set.append(nums[depth]) 
            helper(nums, curr_set, depth+1)
            # Then, we do the case where we don't consider it, and we don't consider the rest of the same 
            # elements as well
            val = curr_set.pop()
            while depth + 1 < len(nums) and nums[depth+1] == val:
                depth += 1
            helper(nums, curr_set, depth+1)

        helper(nums, [], 0)
        return subsets
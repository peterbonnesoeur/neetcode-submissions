class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
            The subarrays are NON sorted and also can have negative number
            -> cannot be too smart with exclusion policies.

            I would say go for a global sum ( 1 time trasversal) then, a 2 pointer scheme.
            This looks a bit like a dp problem

            my_sum = sum(nums)

            if my_sum == k:
                res += 1
            for i in range(len(nums)):
                for j in range(i, len(nums)):


        """
        res = 0
        prefix_sum = {0: 1}
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            # if curr_sum == k:
            #     res += prefix_sum.get(0)
            
            diff = curr_sum - k
            res += prefix_sum.get(diff, 0)
            
            prefix_sum[curr_sum] = prefix_sum.get(curr_sum, 0) + 1

            
        return res

    def subarraySumMeh(self, nums: List[int], k: int) -> int:
        """
            The subarrays are NON sorted and also can have negative number
            -> cannot be too smart with exclusion policies.

            I would say go for a global sum ( 1 time trasversal) then, a 2 pointer scheme.
            This looks a bit like a dp problem

            my_sum = sum(nums)

            if my_sum == k:
                res += 1
            for i in range(len(nums)):
                for j in range(i, len(nums)):


        """
        res = 0
        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                if sum == k:
                    res += 1
        return res

    def subarraySumBruteForce(self, nums: List[int], k: int) -> int:
        
        res = 0

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if sum(nums[i:j + 1]) == k:
                    res += 1

        return res
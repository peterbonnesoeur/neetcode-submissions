class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
            We want to find all the possibilities such that the total sum equals target
            that means that we either ADD or SUBTRACT a num to an ongoing sum.

            This is a 2^n problem.

            target can be negative but the numbers are always positive.

            Let's first do the dfs approach and tehn, try to get smart by using memorization
        """

        # What do we want to memorize?
        # The boundaries first: N elements
        # Maximum amount of values: from -sum(nums) to sum(nums) so 2*sum(nums) + 1 for 0
        
        # In case there is dp[]

        #  2 1 0 -1 -2
        #1 
        #1

        dp = dict()
        def dfs(i: int, currTarget: int) -> int:
            """ 
                DFS traversal of the array
            """

            if i == len(nums) and currTarget == 0:
                return 1
            
            if i >= len(nums):
                return 0

            if (i, currTarget) in dp:
                return dp[(i, currTarget)]

            dp[(i, currTarget)] = dfs(i+1, currTarget - nums[i]) + dfs(i+1, currTarget + nums[i])
            return dp[(i, currTarget)]

        return dfs(0, target)
        
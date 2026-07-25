class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
            The goal is to find IF we can make a partition
            Of an array into 2 arrays such that the sum of each is 
            equal to the sum of the other.

            return false otherwise.

            The numbers are also strictly positive
            We can do the problem firsthand by assigning the numbers to
            array A or the other and when wee reach n, we simply check
            if sum(array_a) == sum(array_b). -> o(2**n)
            Then, I would try to add some memorization.

            edge case:
            [] [0, 0, 0, 0, 0] We can have an empty array after all

            Now, this is not scalable, let's try to add some memory to this
        """
        n : list[int] = len(nums)

        total : int = sum(nums)
        if total % 2 == 1:
            return False

        target: int = total//2 # soit malin dans l'enoncé
        # memo: list[list[int]] = [[-1] * (target + 1) for _ in range(n)] # reste bête, tu veux juste
        # memoriser le probleme là
        memo = dict()
        def dfs(i: int, target: int):

            if target == 0:
                return True
            if i >= n or target < 0:
                return False
            if (i, target) in  memo:
                return memo[(i, target)]

            memo[(i, target)] = dfs(i + 1, target) or dfs(i + 1, target - nums[i])

            return memo[(i, target)]

        return dfs(0, target)

        
        # def helper(depth: int, array_a):
        #     if depth >= N:
        #         return False

        #     currSum = sum(array_a)
        #     if currSum > target:
        #         return False
            
        #     if cache[target - currSum][N - depth - 1] != -1:
        #         return True
            
        #     # set that there IS a sum of elements 
        #     cache[currSum][depth] = 1

        #     decision_a = helper(depth+1 , array_a + [nums[depth]])
        #     decision_b = helper(depth+1 , array_a)

        #     return decision_a or decision_b

        return helper(0, [])
        
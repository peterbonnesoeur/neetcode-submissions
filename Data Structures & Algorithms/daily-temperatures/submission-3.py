class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
            We want to check the number of day after the ith day with warmer
            temp.
            It makes more sense to start thus by the end and create a stack where
            we will be keeping 2 things:
            1 - the temperature
            2 - the index of the said temp

            We will keep such stack monotonic and empty it when we find higher temp
            At the end, we shall reverse the array
        """
        stack = []
        res = []

        for i in range(len(temperatures) - 1, -1, -1):

            while stack and stack[-1][0] <= temperatures[i]:
                stack.pop()

            if stack:
                res.append(stack[-1][1] - i)
            else:
                res.append(0)
            
            stack.append([temperatures[i], i])

        return res[::-1]
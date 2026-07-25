class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
            Function to find the longest common subsequence between 2 non empty
            strings.

            This problem is a decision tree where we choose to either search in the
            subset of text1 or in the one of text2
        """

        dp : dict[tuple(int), int]= {}
        def helper(index1: int, index2:int) -> int:
            """
                Function return the longest common subsequence from the 2 
                indexes passed above
            """

            if index1 == len(text1) or index2 == len(text2): 
                # end of the array -> stop searching/out of bound
                return 0

            if (index1, index2) in dp:
                return dp[(index1, index2)]
            if text1[index1] == text2[index2]:
                dp[(index1, index2)] = 1 + helper(index1 + 1, index2 + 1)
            else:
                #Pick the max subarray between these 2 options
                incr1 = helper(index1 + 1, index2)
                incr2 = helper(index1, index2 + 1)
                dp[(index1, index2)] = max(incr1, incr2)
            return dp[(index1, index2)]
        return helper(0,0)
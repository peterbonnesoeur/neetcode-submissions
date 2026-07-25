from typing import Optional, List

class Solution:
    def _count_zeroes_ones(self, string: str) -> tuple:
        return (string.count("0"), string.count("1"))

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        """
            Function to find the largest subset so that there
            are at most m 0's total and n 1's total by accumulating this subset

            Let's first do a dfs approach, where we will simply choose to pick a 
            subset or discard it.

            Then, we will work on a dp approach with memorization
        """

        zeroes_ones_counter: dict[str, tuple[int]] = dict()

        # Now, there is a lot of repetition that we can prevent.
        # We can keep track of the values for (i, curr_zeroes, curr_ones)

        dp : dict[tuple[int], int]= dict()

        def dfs(i, curr_zeroes: int, curr_ones: int) -> int:
            """
                Traversal of the arrays of strings to detect the length of the max subset 
                of them that are countained within curr_zeroes and curr_ones
            """

            if i == len(strs):
                return 0

            if (i, curr_zeroes, curr_ones) in dp:
                return dp[(i, curr_zeroes, curr_ones)]

            if strs[i] not in zeroes_ones_counter:
                zeroes_ones_counter[strs[i]] = self._count_zeroes_ones(strs[i])

            array_zeroes, array_ones = zeroes_ones_counter[strs[i]]
            
            # Option 1: Skip current string
            res = dfs(i+1, curr_zeroes, curr_ones)
            
            # Option 2: Include current string (if budget allows)
            if curr_zeroes >= array_zeroes and curr_ones >= array_ones:
                res = max(res, 1 + dfs(i+1, curr_zeroes - array_zeroes, curr_ones - array_ones))

            dp[(i, curr_zeroes, curr_ones)] = res
            return res

        return dfs(0, m, n)
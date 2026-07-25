import functools


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:      
        
          
        @functools.lru_cache(None)
        def dfs(index1: int, index2:int) -> int:
            if index1 == len(word1):
                # just return the difference of length and it index, we simply
                # add stuff
                return len(word2) - index2
            
            if index2 == len(word2):
                # We remove stuff from word1
                return len(word1) - index1

            if word1[index1] == word2[index2]:
                return dfs(index1 + 1, index2 + 1)
            else:
                case_replace = 1 + dfs(index1 + 1, index2 + 1)
                case_remove = 1 + dfs(index1 + 1, index2)
                case_add = 1 + dfs(index1, index2 + 1)

                return min(case_replace, case_add, case_remove)

        return dfs(0, 0)
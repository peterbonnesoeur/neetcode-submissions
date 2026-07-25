class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
            Count the number of distinct subsequences res
            such that res is equal to the distinct subsequences of s which are in t
            in case no entries of s are in t, return 0
        """


        dp: dict[tuple(int), int] = {}
        def helper(index_s: int, index_t:int) -> int:

            if index_s >= len(s) or index_t >= len(t):
                return 0

            if (index_s, index_t) in dp:
                return dp[ (index_s, index_t)]
            
            # if index_t >= len(t):
            #     return 1

            found = 0
            if index_t == len(t) - 1 and t[index_t] == s[index_s]:
                found = 1
            
            if t[index_t] == s[index_s]:
                # also consider the case where we are NOT taking this index with us.
                # ex: s: (ca)aat t: (ca)t -> we might want to get s: (c)a(a)at - t: (ca)t
                dp[ (index_s, index_t)] =  found + helper(index_s + 1, index_t + 1) + helper(index_s +1, index_t)
            else:
                # My assumption here is that we never want to increment index_t if no match
                dp[ (index_s, index_t)] =  helper(index_s + 1, index_t)

            return dp[ (index_s, index_t)]
        
        return helper(0,0)
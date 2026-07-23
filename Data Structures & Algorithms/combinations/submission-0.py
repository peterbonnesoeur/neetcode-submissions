class Solution:


    def helper(self, i: int, currComb: list[int], combs:list[int], n: int, k: int) -> None:
        
        # We escape in case we reached the desired length
        if len(currComb) == k:
            combs.append(currComb.copy())
            return
        
        # early stopping to prevent an infinite array of []
        if i > n:
            return
        
        # There, we restrain the possibility
        # As we don't want duplicates, we prevent duplicates
        # such as [1,5] and [5,1] -> this is the way
        for possibility in range(i, n+1):
            currComb.append(possibility)
            self.helper(possibility+1, currComb, combs,n, k)
            currComb.pop()



    def combine(self, n: int, k: int) -> List[List[int]]:
        combs = []
        self.helper(1, [], combs, n, k)
        return combs
class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        """
            This is an implementation of dfs where we remember the
            current path and that is it.
            The goal is to count and add the paths base on the path taken.

            I can memorise the path taken by putting values such as -1 for example and resetting it when I return this step
        """

        R = len(grid)
        C = len(grid[0])
        MOVEMENTS = [[-1,0], [1,0], [0,-1], [0,1]]

        def dfs(r:int, c: int) -> int:

            if r < 0 or r >= R or c < 0 or c >= C:
                return 0

            if grid[r][c] != 0:
                return 0
            
            if r == R-1 and c == C-1:
                return 1

            grid[r][c] = -1
            counter = 0
            for (nc, nr) in MOVEMENTS:
                counter += dfs(r + nr, c + nc)
            grid[r][c] = 0
        
            return counter
        
        return dfs(0, 0)

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        R = len(grid)
        C = len(grid[0])
        MOVEMENTS = [(1,0), (-1,0), (0, 1), (0,-1)]

        r, c = 0, 0
      
        i = 0
        while i < R*C:
            r = i % R
            c = i // R
            # print(r,c)
            if grid[r][c] == 1:
                break

            i+=1
        

        
        print(r,c, grid[r][c])
        def dfs(r: int, c: int) -> int:
            if r<0 or r >= R or c<0 or c >= C or grid[r][c] == 0:
                return 1

            if grid[r][c] != 1:
                return 0
            
            grid[r][c] = -1
            
            perimeter = 0
            for (nr, nc) in MOVEMENTS:
                perimeter += dfs(r + nr, c + nc)

            return perimeter

        return dfs(r, c)
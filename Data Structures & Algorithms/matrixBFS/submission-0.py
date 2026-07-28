from collections import deque

class Solution:

    def shortestPath(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        MOVEMENTS = [[-1,0], [1,0], [0,-1], [0,1]]

        q = deque()

        q.append([0,0])

        length = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                if r < 0 or r >= R or c < 0 or c >= C:
                    continue

                if grid[r][c] != 0:
                    continue
                
                if r == R-1 and c == C-1:
                    return length

                grid[r][c] = -1
                for (nr, nc) in MOVEMENTS:
                    q.append((r+nr, c+ nc))
            length +=1
        
        return -1
        
        return dfs(0, 0)
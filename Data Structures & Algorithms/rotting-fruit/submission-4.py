from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """ Multi source bfs
        
        What ifs:
        - what if there are no rotten fruit ? -> return -1
        """
        
        MOVEMENTS = [(-1,0),(1,0), (0, -1), (0,1)]

        q: deque[tuple[int]] = deque()
        fresh_fruit = 0
        time = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh_fruit +=1
                elif grid[r][c] == 2:
                    q.append((r, c))

        print(q, fresh_fruit)

        if fresh_fruit == 0:
            return 0
        

        if len(q) == 0:
            return -1
        
        fresh_fruit_past = fresh_fruit
        while True:
            new_q = deque()
            while len(q) > 0:
                r, c = q.popleft()
                for movement in MOVEMENTS:
                    nr = r + movement[0]
                    nc = c + movement[1]
                    if nr<0 or nr >= len(grid):
                        continue
                    if nc<0 or nc >= len(grid[0]):
                        continue

                    if grid[nr][nc] == 1:
                        new_q.append((nr, nc))
                        grid[nr][nc] = 2
                        fresh_fruit -= 1
            
            if fresh_fruit == fresh_fruit_past:
                return -1
            
            time +=1
            if fresh_fruit == 0:
                return time
            fresh_fruit_past = fresh_fruit

            q = new_q

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """

            We want to know if we visited an island at least one. 
            When we 'land on an highland, we 'run' through it and record all the places as
            visited places.
            So that if we touch it again in the future and we visited it, we can say with confidence 
            that we were there before and continue our journey.

            Space complexity: O(n^2)

            DFS complexity: O(n^2)
        """

        visited : set[tuple[int]] = set()
        ALLOWED_MOVEMENTS : list[tuple[int]] = [(-1,0), (1, 0), (0, -1), (0, 1)]
        num_islands = 0

        def dfs(r_id: int, c_id: int) -> None:
            if r_id < 0 or r_id >= len(grid):
                return
            if c_id < 0 or c_id >= len(grid[0]):
                return

            if (r_id, c_id) in visited:
                return
            elif grid[r_id][c_id] == "1":
                visited.add((r_id, c_id))
                for movement in ALLOWED_MOVEMENTS:
                    dfs(r_id + movement[0], c_id + movement[1])
        

        for r_id in range(len(grid)):
            for c_id in range(len(grid[0])):
                if grid[r_id][c_id] == "1" and (r_id, c_id) not in visited:
                    dfs(r_id, c_id)
                    num_islands +=1
        
        return num_islands

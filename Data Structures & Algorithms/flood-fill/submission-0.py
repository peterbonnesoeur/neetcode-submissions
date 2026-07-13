class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        """
            sounds like a dfs in such case.

            if target == color -? we will just change the original color
            So we don't run it
        """
        def dfs(r_id: int, c_id: int, target: int):
            if r_id < 0 or r_id >= len(image):
                return
            if c_id < 0 or c_id >= len(image[0]):
                return
            
            if image[r_id][c_id] == target:
                image[r_id][c_id] = color
            else:
                return

            positions: list[tuple[int]] = [(-1,0), (0,1),(1,0), (0,-1)]
            for position in positions:
                dfs(r_id + position[0], c_id+position[1], target)
            

        target = image[sr][sc]
        if target != color:
            dfs(sr, sc, target)
        return image
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
            Two pointer approach -> we can calculate the "area" by doing min(heights(r), heights(l))*(r-l)
            for the moving strategy, we move in priority the height that is the lowest, as there is a chance to 
            be a bigger wall

            time complexity: n

        """

        l, r = 0, len(heights)-1

        max_water = 0
        while l<r:
            lowest_wall = min(heights[l], heights[r])
            max_water = max(max_water, lowest_wall*(r-l))

            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        
        return max_water


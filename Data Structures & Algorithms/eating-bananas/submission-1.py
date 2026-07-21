import math

class Solution:
    def canEatInHours(self, piles:list[int], eat_speed: int) -> int:
        num_hours: int = 0
        for size in piles:
            num_hours += math.ceil(size/eat_speed)
        
        return num_hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = 1, max(piles)

        res = r
        while l<=r:
            mid = (r+l) // 2
            num_hours = self.canEatInHours(piles, mid) 
                     
            if num_hours <= h:
                r = mid - 1
                res = mid
            else:
                l = mid + 1

                
        return res
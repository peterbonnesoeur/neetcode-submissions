
from functools import lru_cache
class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        """
            Compute the maximum profit that one can achieve without exceeding a backpack capacity

            profit and weight are always positive

            Sounds a lot like a greedy problem. We want to maximise the profit vs the weight
            We can do that by using p/w to have the highest profit for the minimum weight.
            This issue also doesnot allow us to reiterate on the same item.

            I would first create my heuristic, sort it, then do a trasversal of the sorted
            results and add greedily the items with the highest ratio first until my capacity is full
        """



        # cache : dict[tuple(int, int), int] = dict()
        @lru_cache(maxsize = len(profit) * capacity)
        def dfs(i: int, curr_capacity:int) -> int:
            if i >= len(profit):
                return 0

            curr_profit = dfs(i+1, curr_capacity)

            if (curr_capacity - weight[i]) >= 0:
                taken_non_excluded = profit[i] + dfs(i, curr_capacity- weight[i])
                curr_profit =  max(curr_profit, taken_non_excluded)
            return curr_profit
 
        
        val =  dfs(0, capacity)
        return val
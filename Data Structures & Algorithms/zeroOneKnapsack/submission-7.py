import heapq
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
        @lru_cache(None)
        def dfs(i: int, curr_capacity:int) -> int:
            if i >= len(profit):
                return 0

            # if (i, curr_capacity) in cache:
            #     return cache[(i, curr_capacity)]
    
            # cache[(i, curr_capacity)] = dfs(i+1, curr_capacity)
            curr_profit = dfs(i+1, curr_capacity)

            if (curr_capacity - weight[i]) >= 0:
                taken = profit[i] + dfs(i+1, curr_capacity- weight[i])
                # cache[(i, curr_capacity)] = max(taken, cache[(i, curr_capacity)])
                curr_profit =  max(taken, curr_profit)
            return curr_profit
 
        
        val =  dfs(0, capacity)
        return val

    def maximumProfitOld(self, profit: List[int], weight: List[int], capacity: int) -> int:
        """
            Compute the maximum profit that one can achieve without exceeding a backpack capacity

            profit and weight are always positive

            Sounds a lot like a greedy problem. We want to maximise the profit vs the weight
            We can do that by using p/w to have the highest profit for the minimum weight.
            This issue also doesnot allow us to reiterate on the same item.

            I would first create my heuristic, sort it, then do a trasversal of the sorted
            results and add greedily the items with the highest ratio first until my capacity is full
        """

        dp = [0] * (capacity +1)

        for p, w in zip(profit, weight):
            for c in range(capacity, -1, -1):
                if c - w >=0:
                    dp[c] = max(dp[c], p + dp[c-w])

        return dp[capacity]

        N, M = len(profit), capacity
        cache = [[-1] * (M + 1) for _ in range(N)]

    
        def dfs(i: int, curr_capacity:int, cache: list[list[int]]) -> int:
            if i >= len(profit):
                return 0

            if cache[i][curr_capacity] != -1:
                return cache[i][curr_capacity]

            #Step 1 : skip the element
            cache[i][curr_capacity] = dfs(i+1, curr_capacity, cache)

            #step 2 - include the current capacity if it fits
            if curr_capacity - weight[i] >= 0:
                p = profit[i] + dfs(i+1, curr_capacity - weight[i],  cache)
                cache[i][curr_capacity] = max(p, cache[i][curr_capacity])
            
            return cache[i][curr_capacity]
 
        
        val =  dfs(0, capacity, cache)
        return val
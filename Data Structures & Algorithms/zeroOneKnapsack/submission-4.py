import heapq

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
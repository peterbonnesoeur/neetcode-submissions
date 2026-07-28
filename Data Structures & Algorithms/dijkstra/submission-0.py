import heapq
from collections import defaultdict

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        """
            Djistra implementation of the shortest path algorithm

            First, we create our adjacency list to track which node goes where 
            Then, we init a structure to keep track of the longest path needed to reach node 
            dest
            Then, we iterate over the next connection of our graph through an heap of the non visited paths.
            if len(res) == n or heap = [] --> stop the algo

            We can also empty the adjacency list after a first visit to prevent doing loops
        """

        adjacency_list = defaultdict(list)
        for edge in edges:
            adjacency_list[edge[0]].append((edge[2], edge[1]))

        # if len(adjacency_list) != n:
        #     return -1

        min_heap = [(0, src)]
        res = dict()

        while min_heap and len(res) != n:
            weight, dest = heapq.heappop(min_heap)
            
            if dest not in res:
                res[dest] = weight
                for new_weight, new_dest in adjacency_list[dest]:
                    heapq.heappush(min_heap, (weight + new_weight, new_dest))
                adjacency_list[dest] = []

        for i in range(n):
            if i not in res:
                res[i] = - 1
        
        return res
        
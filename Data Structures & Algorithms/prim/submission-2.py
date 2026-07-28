from collections import defaultdict
import heapq

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        

        adjacency_list = defaultdict(list)
        for src, dest, weight in edges:
            adjacency_list[src].append((weight, dest))
            adjacency_list[dest].append((weight, src))

        min_heap = [(0,0)]
        visited = set()
        minimum_spanning_weight = 0

        while min_heap:
            weight, dest  = heapq.heappop(min_heap)
            if dest in visited:
                continue
            for (new_weight, new_dest) in adjacency_list[dest]:
                heapq.heappush(min_heap, (new_weight, new_dest))
            minimum_spanning_weight += weight
            visited.add(dest)


        return minimum_spanning_weight if len(visited) == n else -1
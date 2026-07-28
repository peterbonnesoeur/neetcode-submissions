from collections import defaultdict

class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for src, dst in edges:
            adj[src].append(dst)

        topSort = []
        visited = set()  # Visited nodes
        visiting = set() # Nodes being visited in the current DFS call (used to detect cycles)

        def dfs(src: int) -> bool:
            if src in visited: 
                return False
            
            if src in visiting:
                return True # a cycle is detected

            visiting.add(src)
            for neighbor in adj[src]:
                if dfs(neighbor):
                    return True
            
            visiting.remove(src)
            visited.add(src)
            topSort.append(src)

        for i in range(n):
            if dfs(i):
                return []

        topSort.reverse()
        return topSort
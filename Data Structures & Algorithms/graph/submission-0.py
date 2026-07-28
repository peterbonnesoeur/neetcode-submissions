from collections import defaultdict

class Graph:
    
    def __init__(self):
        self.edges = defaultdict(set)


    def addEdge(self, src: int, dst: int) -> None:
        self.edges[src].add(dst)


    def removeEdge(self, src: int, dst: int) -> bool:
        """
            Remove an edge from a source.
            Neither may or may not be in the graph
        """
        if src in self.edges:
            if dst in self.edges[src]:
                self.edges[src].remove(dst)
                return True
        
        return False


    def hasPath(self, src: int, dst: int) -> bool:

        visited = set()

        def dfs(src: int, target: int) -> bool:
            """ 
                Depth first seatrch function to find if there 
                is a a path between src and target with memory
                to prevent visiting twice the same edge   
            """
            for dst in self.edges[src]:
                if dst == target:
                    return True
    
                if dst in visited:
                    continue
                else:
                    visited.add(dst)
                    if dfs(dst, target):
                        return True
            
            return False
        
        return dfs(src, dst)


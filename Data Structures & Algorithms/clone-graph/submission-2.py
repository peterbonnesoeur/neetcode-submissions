"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if node is None:
            return None

        seen_nodes = dict()

        def dfs(node: Node) ->Node:
            if node in seen_nodes:
                return seen_nodes[node]
            
            copy = Node(node.val)
            seen_nodes[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            
            return copy

        def bfs(node: Node) -> Node:
            
            if not node:
                return None

            seen_nodes[node] = Node(node.val)
            q = deque()
            q.append(node)

            while q:
                curr = q.popleft()
                for nei in curr.neighbors:
                    if nei not in seen_nodes:
                        seen_nodes[nei] = Node(nei.val)
                        q.append(nei)

                    seen_nodes[curr].neighbors.append(seen_nodes[nei])
            
            return seen_nodes[node]

            # for neighbor in node.neighbors:
            #     if neighbor in seen_nodes:
            #         new_node.neighbors.append(seen_nodes[neighbor])
            #     else:
            #         # print(seen_nodes)
            #         new_neighbor = Node(neighbor.val)
            #         new_node.neighbors.append(new_neighbor)
            #         seen_nodes[neighbor] = new_neighbor
            #         dfs(neighbor, new_neighbor)

        
        copy_node = bfs(node)
        return copy_node
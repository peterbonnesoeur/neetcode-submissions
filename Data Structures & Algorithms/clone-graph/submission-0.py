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

        def dfs(node: Node, new_node: Node):
            for neighbor in node.neighbors:
                if neighbor in seen_nodes:
                    new_node.neighbors.append(seen_nodes[neighbor])
                else:
                    # print(seen_nodes)
                    new_neighbor = Node(neighbor.val)
                    new_node.neighbors.append(new_neighbor)
                    seen_nodes[neighbor] = new_neighbor
                    dfs(neighbor, new_neighbor)

        
        new_node = Node(node.val)
        seen_nodes[node] = new_node

        dfs(node, new_node)
        return new_node
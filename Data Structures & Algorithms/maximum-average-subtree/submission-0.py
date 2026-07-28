# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    
    max_average: int = 0
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        """
            Max average of each subtree
            This sounds like a dfs problem in post_order

            We want to return the sum and amount of nodes from each subtree
            to prevent a rounding error by the end.
        """
        

        def dfs(node: Optional[TreeNode]) -> tuple(int, int):

            if node is None:
                return 0, 0

            sum_right, count_right = dfs(node.right)
            sum_left, count_left = dfs(node.left)

            sum_node = sum_right + node.val + sum_left
            count_node = count_right + 1 + count_left

            self.max_average = max(self.max_average, sum_node/count_node)

            return sum_node, count_node

        dfs(root)
        return self.max_average
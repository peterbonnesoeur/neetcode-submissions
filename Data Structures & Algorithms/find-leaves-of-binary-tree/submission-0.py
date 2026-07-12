# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        

        old_set : set[Optional[TreeNode]] = set()
        old_set.add(None)
        leaf_set : set[Optional[TreeNode]]= set()
        res : list[list[int]] = []

        def dfs(node: Optional[TreeNode]):
            # print(old_set)
            if node is None:
                return
            if node in old_set:
                return
            if node.left in old_set and node.right in old_set:
                leaf_set.add(node)
            
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        while len(leaf_set) > 0:
            res.append([leaf.val for leaf in leaf_set])
            old_set.update(leaf_set)
            leaf_set = set()
            dfs(root)
            # res.append([leaf.val for leaf in leaf_set])
        

        return res
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
            This is a walk the tree problem, an easy way yo do this
            is to keep a datastructure, like a hash map
            and use its index to store a x coordinate and in value, put
            the array of answers.

            Them, we can reconstruct the array by the end
            O(2n) space
            O(n) trasversal
        """

        tree_trasversal = defaultdict(list)

        def bfs(node: Optional[TreeNode]) -> None:


            q = deque()

            if node is None:
                return 0

            min_index = 0
            q.append((node, 0))

            while q:
                for i in range(len(q)):
                    node, index = q.popleft()

                    tree_trasversal[index].append(node.val)

                    if node.left:
                        q.append((node.left, index - 1))
                        min_index = min(min_index, index - 1)
                    if node.right:
                        q.append((node.right, index + 1))

            return min_index
            # if node is None:
            #     return None

            # tree_trasversal[index].append(node.val)
            # left_min_index = dfs(node.left, index - 1)
            # right_min_index = dfs(node.right, index + 1)

            # if left_min_index is None:
            #     left_min_index = index

            # if right_min_index is None:
            #     right_min_index = index
            # return min(index, left_min_index , right_min_index)

        index = bfs(root)

        res : list[int] = []
        while index in tree_trasversal:
            res.append(tree_trasversal[index])
            index += 1

        return res

            
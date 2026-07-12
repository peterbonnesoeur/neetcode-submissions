# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        

        pairs: list[tuple(int, int)] = []

        def getHeight(node: Optional[TreeNode]) -> int:
            # print(old_set)
            if node is None:
                return -1
            
            left_height: int = getHeight(node.left)
            right_height: int = getHeight(node.right)

            curr_height: int = max(left_height, right_height) + 1
            pairs.append((curr_height, node.val))
            return curr_height

        getHeight(root)

        if len(pairs) == 0:
            return []

        pairs.sort(key= lambda x: x[0], reverse = True)

        print(pairs)
        curr_height: int = pairs[0][0]
        i: int = 0

        res = []
        while curr_height >= 0:
            # print(curr_height)
            curr_res = []
            while i < len(pairs) and pairs[i][0] == curr_height:
                curr_res.append(pairs[i][1])
                i+=1
            res.insert(0, curr_res)
            curr_height -= 1
        return res

    
    def findLeaves1(self, root: Optional[TreeNode]) -> List[List[int]]:
        

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
        

        return res
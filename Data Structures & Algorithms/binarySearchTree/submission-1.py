from typing import Optional

class Node:

    def __init__(self, key: int, val: int, right: Optional[Node] = None, left: Optional[Node] = None):
        self.right = right
        self.left = left
        self.val = val
        self.key = key


class TreeMap:
    
    def __init__(self):
        self.size = 0
        self.root = None

    def insert(self, key: int, val: int, ) -> None:
        node = Node(key, val)
        if self.root == None:
            self.root = node
            return

        current = self.root 
        while True:
            if key == current.key:
                current.val = val
                return
            elif key < current.key:
                if current.left == None:
                    current.left = node
                    return
                current = current.left
            else: 
                if current.right == None:
                    current.right = node
                    return
                current = current.right


    def get(self, key: int) -> int:
        current = self.root
        while current != None:
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                return current.val
        return -1

    def getMin(self) -> int:
        current = self.findMin(self.root)
        return current.val if current else -1

    # Returns the node with the minimum key in the subtree
    def findMin(self, node: TreeNode) -> TreeNode:
        while node and node.left:
            node = node.left
        return node

    def getMax(self) -> int:
        node = self.root

        while node and node.right:
            node = node.right
        
        if node is not None:
            return node.val
        else:
            return -1


    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)

    # Returns the new root of the subtree after removing the key
    def removeHelper(self, curr: TreeNode, key: int) -> TreeNode:
        if curr == None:
            return None

        if key > curr.key:
            curr.right = self.removeHelper(curr.right, key)
        elif key < curr.key:
            curr.left = self.removeHelper(curr.left, key)
        else:
            if curr.left == None:
                # Replace curr with right child
                return curr.right
            elif curr.right == None:
                # Replace curr with left child
                return curr.left
            else:
                # Swap curr with inorder successor
                minNode = self.findMin(curr.right)
                curr.key = minNode.key
                curr.val = minNode.val
                curr.right = self.removeHelper(curr.right, minNode.key)
        return curr

    def getInorderKeys(self) -> List[int]:
        result = []
        self.inOrderTraversal(self.root, result)
        return result

    def inOrderTraversal(self, node, result) -> None:
        if node != None:
            self.inOrderTraversal(node.left, result)
            result.append(node.key)
            self.inOrderTraversal(node.right, result)


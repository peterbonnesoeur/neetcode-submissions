class Node:

    def __init__(self, val:int) -> None:
        self.val: int = val
        self.parent: int = val
        self.rank = 0

    def __str__(self) -> str:
        return f"val {self.val} - parent: {self.parent} - rank: {self.rank}"

class UnionFind:
    
    def __init__(self, n: int):
        self.array = [Node(x) for x in range(n)]
        self.num_components = n
        

    def find(self, x: int) -> int:
        curr_node = self.array[x]
        if curr_node.parent == curr_node.val:
            return curr_node.val
        else:
            curr_node.parent = self.find(curr_node.parent)
            return curr_node.parent
        

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        x_el = self.array[self.find(x)]
        y_el = self.array[self.find(y)]


        if (x_el.val != y_el.parent) and (y_el.val != x_el.parent):
            if x_el.rank < y_el.rank:
                # y_el.parent = self.array[y_el.parent].parent
                x_el.parent = y_el.val
                y_el.rank += 1
            else:
                # Small optim -> faster search -> up the 
                # if x_el.parent != x_el.val:
                # x_el.parent = self.array[x_el.parent].parent
                x_el.rank += 1
                y_el.parent = x_el.val
                
            self.num_components -= 1
            return True
        return False
        

    def getNumComponents(self) -> int:
        return self.num_components


import heapq

class UnionFind:

    def __init__(self, n):
        self.par = {}
        self.rank = {}
        for i in range(1, n+1):
            self.par[i] = i
            self.rank[i] = 0

    def find(self, n):
        p = self.par[n]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]] 
            # we update the parent of the intermediate nodes
            p = self.par[p]
        return p

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p1] = p2
            self.rank[p2] += 1

        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        union_util = UnionFind(len(points))
        edges = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                manhatan_dist = abs(points[i][0] -points[j][0]) + abs(points[i][1] -points[j][1]) 
                edges.append((manhatan_dist, i+1, j+1))

        heapq.heapify(edges)
        mst = []

        while len(mst) < len(points)-1:
            weight, n1, n2 = heapq.heappop(edges)
            if not union_util.union(n1, n2):
                continue
            mst.append(weight)
        
        return sum(mst)
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        res = []
        for i in range(numRows):
            if i == 0:
                res.append([1])
            else:
                row = [1]
                for j in range(1, i):
                    row += [res[-1][j - 1] + res[-1][j]]
                row += [1]
                res.append(row)
            
        return res
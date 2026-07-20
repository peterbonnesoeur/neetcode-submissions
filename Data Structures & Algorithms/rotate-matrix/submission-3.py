class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix)-1

        for i,col in enumerate(zip(*matrix[::-1])):
            print(col)
            matrix[i] = col
        
        # return
        # while l<r:
        #     for i in range (r-l):
        #         top_left = matrix[l][l+i]
        #         ## move bottom left into top left
        #         matrix[l][l+i] = matrix[r-i][l]
        #         #bottom right into bottom left
        #         matrix[r-i][l] = matrix[r][r-i]
        #         #top tight into bottom left 
        #         matrix[r][r-i] = matrix[l+i][r]
        #         # Top left into top right
        #         matrix[l+i][r] = top_left
        #         # top_right = matrix[i][r]
        #         # bottom_right = matrix[r][r-i]
        #         # bottom_left = matrix[r-i][l]
        #     r -= 1
        #     l += 1
        

        # return matrix
class Solution:
    def confusingNumber(self, n: int) -> bool:
        
        n = str(n)
        if any([char in n for char in ["2", "3", "4", "5", "7"]]):
            return False
        new_n = n
        # replace the 6 by #
        new_n = new_n.replace("6", "#")
        new_n = new_n.replace("9", "6")
        new_n = new_n.replace("#", "9")

        print(n, new_n)
        return new_n[::-1] != n
class Solution:
    def intToRoman(self, num: int) -> str:
        """
            We go from biggest to smallest number
            and simply repeat the patter in case we are in front of
            a low modulus
        """

        symList = [
            ["I", 1], ["IV", 4], ["V", 5], ["IX", 9],
            ["X", 10], ["XL", 40], ["L", 50], ["XC", 90],
            ["C", 100], ["CD", 400], ["D", 500], ["CM", 900],
            ["M", 1000]
        ]
        res : int = ""
        for char, val in reversed(symList):
            multiplier = num // val
            if multiplier > 0:
                res += multiplier * char
                num = num%val

        return res
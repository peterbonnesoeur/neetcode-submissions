class Solution:

    def helper(self, digits_left: list[str], curr_comb: list[str], combs: list[str], value_map: dict[str]) -> None:
        if digits_left == "":
            combs.append(curr_comb)
            return

        for char in value_map[digits_left[0]]:
            curr_comb += char
            self.helper(digits_left[1:], curr_comb, combs, value_map)
            curr_comb = curr_comb[:-1]


    def letterCombinations(self, digits: str) -> List[str]:
        """
            The goal is to give a set of possibilities given some letters
            The first part that comes to mind is combinations with a hash map
            to map the num to some potential letters

            We are going from 2 to 9 only for our hash map,
            each touch is registered and can correspond up to 3 values, 4 values for 9

            Complexity:
            len(digits) = n
            Worst case of possibilities: 4
            4^n
        """

        combs = []
        value_map = {
            "2": "abc",
            "3":"def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        if len(digits) == 0:
            return combs
        self.helper(digits, "", combs, value_map)

        return combs
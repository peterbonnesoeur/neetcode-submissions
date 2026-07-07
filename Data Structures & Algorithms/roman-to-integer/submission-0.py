class Solution:
    def romanToInt(self, s: str) -> int:
        """
            To resolve this, we can do so by keeping a past reminder of a potential
            'amount to deduce' for the next iteration, which would be more memory optimized, but would
            arguably make the code a bit lengthier as we need to remind ourselves of all edge cases.
            I prefer to just map the special cases in priority, this would cost us a bit more memory but makes
            for a more readble code.
            Then, we do a check if the char are in the special case, if not, we do regular cases and we increment a pointer
        """
        conversion_table = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        special_cases = {
            "IV" : 4,
            "IX" : 9,
            "XL" : 40,
            "XC" : 90,
            "CD" : 400,
            "CM" : 900
        }

        i = 0
        res = 0
        while i < len(s):
            special_case_val = special_cases.get(s[i:i+2],0)
            if special_case_val>0:
                i+=2
                res += special_case_val
            else:
                res += conversion_table.get(s[i])
                i += 1

        return res
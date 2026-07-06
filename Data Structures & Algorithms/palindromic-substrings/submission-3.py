from itertools import combinations

class Solution:

    def isPalindrome(self, s) -> bool:
        return s == s[::-1]

    def countSubstrings(self, s: str) -> int:
        """
            A palindrome is an extension of a centroid
        """
        res = 0
        for i in range(len(s)):
            # account for even and odd length palindroms
            for l, r in [(i,i), (i, i+1)]:
                while l>=0 and r< len(s) and s[l] == s[r]:
                    res+=1
                    l-=1
                    r+=1
        
        return res

    def countSubstringsBrute(self, s: str) -> int:
        res = 0
        if len(s) == 1:
            return 1
        for i in range(1,len(s)):
            combis = combinations(s, i)
            for combi in combis:
                if self.isPalindrome("".join(combi)):
                    res+=1
        return res
        # res = 0

        # if self.isPalindrome(s):
        #     res +=1
        
        # for i in range(len(s)):
        #     print(s[:i] + s[i+1:])
        #     res += self.countSubstrings(s[:i] + s[i+1:])
        
        # return res
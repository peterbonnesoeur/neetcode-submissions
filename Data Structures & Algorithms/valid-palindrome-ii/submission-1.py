class Solution:
    def validPalindrome(self, s: str) -> bool:
        return self.palindromeHelper(s, True)

    def palindromeHelper(self, s:str, joker: bool = False):
        l, r = 0, len(s) - 1
        while l<r:
            if s[l] == s[r]:
                l+=1
                r-=1
            else:
                if joker:
                    remove_left = s[:l] + s[l+1:]
                    remove_right = s[:r] + s[r+1:]
                    return self.palindromeHelper(remove_left) or self.palindromeHelper(remove_right)
                else:
                    return False

        return True
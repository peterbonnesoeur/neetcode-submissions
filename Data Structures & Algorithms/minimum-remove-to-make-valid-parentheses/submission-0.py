class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        l, r = 0, 0

        indexes_to_rm = []
        
        while l< len(s):
            if s[l] == ")" and r > l:
                l+=1
            elif s[l] == ")":
                indexes_to_rm.insert(0, l)
                l+=1
            elif s[l] == "(":
                if r<=l:
                    r = l+1
                while r < len(s) and s[r] != ")":
                    r += 1
                if r >= len(s):
                    indexes_to_rm.insert(0, l)
                l+=1
                r+=1
            else:
                l+=1

        for i in indexes_to_rm:
            s= s[:i] + s[i+1:]
        
        return s
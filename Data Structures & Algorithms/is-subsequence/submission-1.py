class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        sub_index = 0
        if len(s) == 0:
            return True
        for i in range(len(t)):
            if s[sub_index] == t[i]:
                print(sub_index, i)
                sub_index+=1
                if sub_index == len(s):
                    return True
        
        return False
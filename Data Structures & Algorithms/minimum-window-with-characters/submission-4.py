from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = dict(Counter(t))
        conditions = {key: False for key in t_count.keys()}

        l, r = 0, 0

        min_window = s

        while r < len(s):
            if s[r] in t_count:
                t_count[s[r]] -= 1
                if t_count[s[r]] <= 0:
                    conditions[s[r]] = True
            
            while sum(conditions.values()) == len(t_count) and l<=r:
                print(s[l:r+1], conditions)
              
    
                while s[l] not in t_count and l<=r:
                    l+=1
                
                if t_count[s[l]]<0:
                    t_count[s[l]]+=1
                    l+=1
                else:
                    if r-l+1 < len(min_window):
                        min_window = s[l:r+1]
                    break
            r+=1

        if sum(conditions.values()) != len(t_count):
            return ""
        return min_window



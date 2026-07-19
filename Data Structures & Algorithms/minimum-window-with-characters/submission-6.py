from collections import Counter

class Solution:
    def condition(self, x: dict[int]) -> bool:
        c : int = 0
        for k, v in x.items():
            if v<=0:
                c+=1
        return c == len(x)

    def minWindow(self, s: str, t: str) -> str:
        t_count = dict(Counter(t))
        conditions = {key: False for key in t_count.keys()}

        l, r = 0, 0
        flag = False

        min_window: str = s

        while r < len(s):
            if s[r] in t_count:
                t_count[s[r]] -= 1

            if self.condition(t_count):
                flag = True
            while flag and l<=r:              
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

        return min_window if flag else ""



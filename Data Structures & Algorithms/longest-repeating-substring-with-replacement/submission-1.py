class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
            Character replacement game
            We could be doing a count with a hashmap
        """
        counter = dict() # Maximum 26 entries
        l, r = 0, 0
        max_length = 0

        maxf = 0

        while r < len(s):
            counter[s[r]] = counter.get(s[r], 0) + 1
            maxf = max(counter[s[r]], maxf)
            while (r - l + 1) - maxf > k :
                counter[s[l]] -= 1
                l+=1
            
            max_length = max(max_length, r - l + 1)
            r+=1

        return max_length
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
            a two pointer implementation sounds like a good idea, with a memory.
            The memory can be a set to remember the unicity of character or a dict.
            I prefer the dict approach.

            Basically, we increment a window and add a letter to the dict with its position. 

            But wait, if we just reset on the dict index, we might not clear the other elements in the set.

            better do a while loop then that clears the set up until the last saw same character
        """

        l = 0
        max_length = 0
        memory = set()

        for r in range(len(s)):
            if s[r] in memory:
                while s[l] != s[r]:
                    memory.remove(s[l])
                    l += 1
                # once we fall on the right term, we just increment it
                l+=1
            else:
                memory.add(s[r])
                max_length = max(max_length, len(memory))
        return max_length
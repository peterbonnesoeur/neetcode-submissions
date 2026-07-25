class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().rsplit(" ", 1)[-1])
class Solution:
    def maxScore(self, s: str) -> int:
        right_sum = maximum = s.count("1")
        if s[0] == "1":
            maximum -=1
        left_sum = 0

        for val in s[:-1]:
            if val == "0":
                left_sum += 1
            else:
                right_sum -=1
            
            maximum = max(maximum, right_sum + left_sum)

        return maximum
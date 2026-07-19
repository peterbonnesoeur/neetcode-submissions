class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
            edge cases:
            - []
            - [[1,2][1,2]]
            - [[1,2], [2, 6], [7,9]]
            - [[1,10],[1,2]]
            We first want to sort the intervals, as this is the only way to
            make the unions without re-looking at the entirety of the array.

        Then we take a current element, the first element of the list

        """

        # if len(intervals) == 1:
        #     return intervals

        intervals.sort()

        result = []
        curr = intervals[0]
        i = 1
        while i < len(intervals):
            if intervals[i][0] > curr[1]:
                result.append(curr)
                curr = intervals[i]
            else:
                curr[1] = max(curr[1], intervals[i][1])

            i+=1

        result.append(curr)
        return result

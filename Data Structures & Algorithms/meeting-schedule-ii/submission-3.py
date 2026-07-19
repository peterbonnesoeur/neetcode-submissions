"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        """
            What interests us here is when the meeting start, fill a structure,
            check that the next meeting begining is before the end of the shortest meeting still 
            in the structure.
            If it is -> we expulse the meeting from the structure, unless I can't anymore.
            Then I had it to my structure.

            Ideally, we want a structure that is acting like a min heap, using the end time as key
            Then, the maximum amount of rooms is "just" the maximum size of the heap during its execution.

            edge case:
            []
            [(0,8),(8,10)]
        """

        intervals.sort(key=lambda x: (x.start, x.end))
        meeting_heap: list[int]  = []
        max_rooms = 0

        i = 0
        while i < len(intervals):
            while meeting_heap and meeting_heap[0] <= intervals[i].start: 
                # the end time of the shortest meeting is inferior to the begining of the next one
                heapq.heappop(meeting_heap)
            
            # We only need to remember when the meeting end
            heapq.heappush(meeting_heap, intervals[i].end)
            max_rooms = max(max_rooms, len(meeting_heap))
            i+=1
        
        return max_rooms
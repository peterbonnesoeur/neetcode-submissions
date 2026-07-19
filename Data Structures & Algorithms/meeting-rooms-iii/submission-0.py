class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        available : list[int] = [i for i in range(n)] # min heap for available rooms
        used : list[tuple[int]] = [] # [(end_time, room_num)] min heap for used rooms
        count = [0] * n

        for start, end in meetings:
            while used and used[0][0] <= start:
                _, room = heapq.heappop(used)
                heapq.heappush(available, room)
            
            if not available:
                end_room, room = heapq.heappop(used)
                end += end_room - start # this is the earliest meeting -> no need to store and
                                        # intermediate state
                heapq.heappush(available, room)
            
            room = heapq.heappop(available)
            heapq.heappush(used, (end, room))
            count[room] += 1
        
        print(count)
        return count.index(max(count))

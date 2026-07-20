# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
            Brute force: -> current list and sort with the next one

            Can we work with heaps ?

            where we have (val, list_index)
            Why list index?
            If we have [1 1 1] [2 , 3] -> I want to automatically, if I pop one element to refill it back with heappush
        """

        cursor = []
        dummy = curr = ListNode(0)

        for i, node in enumerate(lists):
            heapq.heappush(cursor, (node.val, i, node))

        
        i = len(lists) + 1
        # curr = None
        while len(cursor) > 0:
            node = heapq.heappop(cursor)[-1]
            
            curr.next = node
            curr = curr.next

            if node.next is not None:
                heapq.heappush(cursor, (node.next.val, i, node.next))
                i+=1
            
        
        return dummy.next

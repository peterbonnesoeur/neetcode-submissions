# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        

        # Dummy method is strong. We set the target ( our prev)
        # we jump onto the next one ONLY when we have no int matching.
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy

        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return dummy.next

        # curr = head

        # # pre-clean the start
        # # ex: [2, 2, 1] -> head -> 1
        # while curr and curr.val == val:
        #     curr = curr.next
        #     head = curr

        # if not curr:
        #     return head

        # #handle the lonely curr
        # prev = curr
        # curr = curr.next
        # while curr:
        #     if curr.val == val:
        #         #[ 1, 2, 2] / 2 -> prev = 1 -> prev.next = curr.next 
        #         prev.next = curr.next
        #         curr = prev.next
        #     else:
        #         #[ 1, 2, 2] / 2 -> prev = 1 curr = 2
        #         prev = curr
        #         curr = curr.next

        # return head
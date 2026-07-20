# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        fast = slow = head

        k = k%500
        n = k - 1
        if not head:
            return None
        while n >= 0:
            fast = fast.next
            if fast == None:
                fast = head
                
            n -= 1

        while fast and fast.next:
            fast = fast.next
            slow = slow.next

        # We use the fast pointer and make it point to head
        fast.next = head
        temp = slow.next
        slow.next = None

        return temp
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        

        """
        Always need to be an intermitent state

        start as prev = None
        curr = head
        prev -> curr -> next

        temp = curr.next

        curr.next = prev

        prev <-  curr  next == temp
        prev  = curr
        curr = temp
        """
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        
        return prev
        
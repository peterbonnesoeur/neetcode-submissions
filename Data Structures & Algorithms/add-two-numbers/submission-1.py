# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """

        The complexities are the following:
        1 - l1 and l2 can be of different size
        2 - In case l1.val + l2.val > 10, we need to carry over a 1
        """

        res = None
        head = None
        carry = 0

        while l1 or l2 or carry !=0:
            val = None
            if l1:
                val = l1.val
                l1 = l1.next
            if l2:
                if val:
                    val += l2.val
                else: 
                    val = l2.val
                l2 = l2.next

            if val is None:
                if carry == 0:
                    break
                else:
                    val = 0

            if res is None:
                res = ListNode((val + carry)%10)
                head = res
            else:
                head.next = ListNode((val + carry)%10)
                head = head.next
            
            carry = (val+carry)//10
        return res
       

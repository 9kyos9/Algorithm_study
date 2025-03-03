# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        #creating new list
        l3 = ListNode()
        curr = l3
        carry = 0

        while l1 and l2:
            carry, val = divmod(l1.val + l2.val + carry, 10)
            l1 = l1.next
            l2 = l2.next
            curr.next = ListNode(val)
            curr = curr.next
        
        l4 = l1 if l1 else l2

        while l4:
            carry, val = divmod(l4.val+carry, 10)
            l4 = l4.next
            curr.next = ListNode(val)
            curr = curr.next
        
        if carry == 1:
            curr.next = ListNode(1)
        
        return l3.next



        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
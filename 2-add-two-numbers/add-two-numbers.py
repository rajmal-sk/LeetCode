# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        res = None
        dummy_head = ListNode(-1, None)
        curr = dummy_head
        while l1 and l2:
            val = (l1.val + l2.val + carry) % 10
            carry = 1 if l1.val + l2.val + carry >= 10 else 0

            node = ListNode(val)
            curr.next = node
            curr = node

            l1 = l1.next
            l2 = l2.next
        
        while l1:
            val = (l1.val + carry) % 10
            carry = 1 if l1.val + carry >= 10 else 0
            node = ListNode(val)
            curr.next = node
            curr = node
            l1 = l1.next
        
        while l2:
            val = (l2.val + carry) % 10
            carry = 1 if l2.val + carry >= 10 else 0
            node = ListNode(val)
            curr.next = node
            curr = node
            l2 = l2.next
        
        if carry:
            node = ListNode(carry)
            curr.next = node
            curr = node
        
        return dummy_head.next
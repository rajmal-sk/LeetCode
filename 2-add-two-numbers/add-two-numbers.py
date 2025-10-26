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
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            val = (val1+ val2 + carry) % 10
            carry = 1 if val1+ val2 + carry >= 10 else 0

            node = ListNode(val)
            curr.next = node
            curr = node

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        # while l1:
        #     val = (l1.val + carry) % 10
        #     carry = 1 if l1.val + carry >= 10 else 0
        #     node = ListNode(val)
        #     curr.next = node
        #     curr = node
        #     l1 = l1.next
        
        # while l2:
        #     val = (l2.val + carry) % 10
        #     carry = 1 if l2.val + carry >= 10 else 0
        #     node = ListNode(val)
        #     curr.next = node
        #     curr = node
        #     l2 = l2.next
        
        # if carry:
        #     node = ListNode(carry)
        #     curr.next = node
        #     curr = node
        
        return dummy_head.next
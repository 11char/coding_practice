#https://leetcode.com/problems/add-two-numbers/

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, 
    l1: Optional[ListNode], 
    l2: Optional[ListNode],
    carry: int = 0) -> Optional[ListNode]:
        if not l1 and not l2 and carry == 0:
            return None
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        total = v1 + v2 + carry
        node = ListNode(total % 10)
        carry = total // 10

        next1 = l1.next if l1 else None
        next2 = l2.next if l2 else None

        node.next = self.addTwoNumbers(next1,next2,carry)
        return node
# https://leetcode.com/problems/merge-nodes-in-between-zeros/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = head
        ptr2 = head.next
        tmp = 0

        while ptr2:
            if(ptr2.val == 0):
                ptr1 = ptr1.next
                ptr1.val = tmp
                tmp = 0

            else:
                tmp += ptr2.val

            ptr2 = ptr2.next

        ptr1.next = None
        return head.next
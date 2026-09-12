# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        nextNode = head.next
        prevNode = head
        i = 0
        while nextNode is not None:
            n = nextNode.next
            nextNode.next = prevNode
            if i == 0:
                prevNode.next = None
            prevNode = nextNode
            nextNode = n
            i += 1
        return prevNode
            
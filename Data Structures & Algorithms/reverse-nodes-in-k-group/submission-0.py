# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
   def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        ret = ListNode(0)
        new = ret

        while head is not None:

            vals = []
            temp = head
            count = 0

            # Take k elements
            while temp is not None and count < k:
                vals.append(temp.val)
                temp = temp.next
                count += 1

            # Less than k elements -> keep them unchanged
            if count < k:
                while head is not None:
                    new.next = ListNode(head.val)
                    new = new.next
                    head = head.next
                break

            # Reverse this group
            vals.reverse()

            # Add reversed group
            index = 0
            while index < len(vals):
                new.next = ListNode(vals[index])
                new = new.next
                index += 1

            # Move to the next group
            head = temp

        return ret.next
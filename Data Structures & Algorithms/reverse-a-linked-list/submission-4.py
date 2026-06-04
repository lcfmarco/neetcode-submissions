# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # do it iteratively
        
        curr = head

        prev = None

        while curr is not None:
            temp = curr.next # use temp to store our current node so we can use it to find our next node

            # begin the shift

            # Make the current node point towards the previous node
            curr.next = prev

            # Update the previous node to our current node
            prev = curr

            # Update our current node to the next node to process
            curr = temp

        return prev # the new head






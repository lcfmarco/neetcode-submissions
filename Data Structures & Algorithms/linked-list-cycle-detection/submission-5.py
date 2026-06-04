# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        prev_pointer = head
        curr_pointer = head

        while curr_pointer:
            if curr_pointer.next == prev_pointer:
                return True
            elif curr_pointer.next is None:
                return False
            curr_pointer = curr_pointer.next.next
            prev_pointer = prev_pointer.next
        return False
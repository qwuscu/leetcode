# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head

        curr = head
        prev = None

        while curr:
            next = curr.next
            # None -> 1 -> 2 -> 3 -> 4
            #  p      c    n
            curr.next = prev
            prev = curr
            curr = next

        return prev
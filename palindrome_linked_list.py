# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        values = []
        while head:
            values.append(head.val)
            head = head.next

        i = 0
        j = len(values) - 1
        while i < j:
            if values[i] != values[j]:
                return False
            i += 1
            j -= 1
        return True
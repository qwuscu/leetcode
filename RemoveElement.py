# from typing import List
#
# #two pointer, time: O(n), space: O(1)
# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         i = 0
#         j = len(nums)
#         while i < j:
#             if nums[i] == val:
#                 nums[i] = nums[j-1]
#                 j -= 1
#             else:
#                 i += 1
#         return j

class Solution:
    """
    @param: A: A list of integers
    @param: elem: An integer
    @return: The new length after remove
    """
    def removeElement(self, A, elem):
        # write your code here
        i = 0
        j = 0
        for j in range(len(A)):
            if A[j] != elem:
                A[i] = A[j]
                i += 1
        return A[:i]

print(Solution().removeElement([0,4,4,0,0,2,4,4], 4))



class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        i = 0
        for j in range(n):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i
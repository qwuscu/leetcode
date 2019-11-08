from typing import List


# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         # duplicate number may occur more then once
#         left = 1
#         right = len(nums)
#         while left <= right:
#             count = 0
#             # find the mid number
#             mid = left + (right-left)//2
#             # find how many number <= mid
#             for num in nums:
#                 if num <= mid:
#                     count += 1
#             # if count > mid, means duplicate exists in [1,mid)
#             # 因为如果是比mid小的话，小于mid的数就要比mid多（大）
#             if count > mid:
#                 right = mid - 1
#             # means duplicate exist in [mid, len(nums))
#             else:
#                 left = mid + 1
#         return left


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left = 1
        right = len(nums)
        while left < right:
            mid = left + (right-left)//2
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            if count <= mid:
                left = mid + 1
            else:
                right = mid
        return right



print(Solution().findDuplicate([1,3,4,2,2]))
print(Solution().findDuplicate([3,1,3,4,2]))
print(Solution().findDuplicate([1,2,1]))
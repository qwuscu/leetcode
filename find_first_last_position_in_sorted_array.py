from typing import List

#Time complexity : O(logN), base 2 not 10
# space: O(1)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1, -1]
        start, end = 0, len(nums) - 1
        i, j = 0, len(nums) - 1

        while i + 1 < j:
            m = i + (j - i) // 2
            if nums[m] >= target:
                j = m
            else:
                i = m
        if nums[i] == target:
            start = i
        elif nums[j] == target:
            start = j
        else:
            start = -1

        i, j = 0, len(nums) - 1
        while i + 1 < j:
            m = i + (j - i) // 2
            if nums[m] <= target:
                i = m
            else:
                j = m
        if nums[j] == target: # failed at ([2,2,],2) if nums[i] == target => end =i then check nums[j]
            end = j
        elif nums[i] == target:
            end = i
        else:
            end = -1

        return [start, end]


print(Solution().searchRange([5,7,7,8,8,10],8))
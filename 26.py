class Solution:
    #two pointers, time complexity: O(n), spcae: O(1)
    def removeDuplicates(self, nums):
        if not nums: return 0
        i = 0
        for j in range(0, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1

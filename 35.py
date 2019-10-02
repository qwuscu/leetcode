class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        while i < len(nums) and nums[i] <= target:
            if nums[i] == target:
                return i
            i += 1
 
        return i 
  
  class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = start + (end-start)//2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                start = mid + 1
            else:
                end = mid
        if target > nums[end]:
            return end+1
        else:
            return end

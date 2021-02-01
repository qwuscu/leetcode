'''
time:  O(n^3) Three nested loops are there to check every triplet.
space: O(1)
'''
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if (nums[i]+nums[j]>nums[k]) and (nums[k]+nums[j]>nums[i]) and (nums[k]+nums[i]>nums[j]):
                        count += 1
        return count



class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)-1
        count = 0
        for i in range(n, -1, -1):
            left = 0
            right = i-1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    count += right - left
                    right -= 1
                else:
                    left += 1
        return count v
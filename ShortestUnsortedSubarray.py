class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sortedNums = sorted(nums)
        start, end = 0, len(nums)
        while end > 0 and nums[end-1] == sortedNums[end-1]:
            end -= 1
        while start < end and nums[start] == sortedNums[start]:
            start += 1
        return end - start

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sortedNums = sorted(nums)
        ans = len(nums)
        while ans > 0 and nums[ans - 1] == sortedNums[ans - 1]:
            ans -= 1
        temp = 0
        for i in range(ans):
            if nums[i] == sortedNums[i]:
                temp += 1
            else:
                break
        return ans - temp
       

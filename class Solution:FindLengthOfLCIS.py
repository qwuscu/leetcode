class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        res = 1
        i = 1
        while i < len(nums):
        	j = i
        	count = 0
        	while j < len(nums):
        		if nums[j] >= nums[j-1]:
        			count += 1
        		else:
        			count = 0
        		res = max(count, res)
        		j += 1
        	i += 1



print(Solution().findLengthOfLCIS([1,3,5,4,7]))



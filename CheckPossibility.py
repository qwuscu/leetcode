from typing import List

# [4,2,3] -> [2,2,3]
# [4,6,5,5] -> [4,5,5,5] 
# [4,6,3,6] -> [4,6,6,6], 4,3,3 is incorrect 
# time: O(n), we loop the array once
# space: O(1)
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                count += 1
                if i == 1 or nums[i] > nums[i-2]:
                	nums[i-1] = nums[i]
                else:
                	nums[i] = nums[i-1]
        return count<=1


if __name__ == "__main__":
	nums=[2,3,3,2,4]
	print(Solution().checkPossibility(nums))
